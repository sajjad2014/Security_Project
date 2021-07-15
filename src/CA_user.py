import datetime
import json
import ssl
import base64
import requests
from OpenSSL import crypto
from cryptography.hazmat.backends.openssl.backend import backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from flask import Flask

from src.shared_data import SharedData


class AuthenticationError(Exception):
    pass


TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def sign(key, data):
    data_j = json.dumps(data)
    private_key = serialization.load_pem_private_key(
        key.encode('utf-8'),
        backend=backend,
        password=None
    )
    signature = private_key.sign(
        data_j.encode('utf-8'),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature


def check_sign(sign_value, signer_pubkey, data):
    try:
        data_j = json.dumps(data)
        pub_key_obj = serialization.load_pem_public_key(
            signer_pubkey.encode('utf-8'),
            backend=backend
        )
        pub_key_obj.verify(
            sign_value,
            data_j.encode('utf-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256())
        return True
    except:
        return False


def server_auth(func):
    def wrapper_func(self):
        from flask import request, abort, jsonify
        data = {}
        try:
            data = request.get_json()
        except Exception as e:
            print(e)
            abort(400)
        try:
            data, recierver_id = self.remove_auth(data)
            return jsonify(self._add_auth(func(self, data, recierver_id), recierver_id))
        except AuthenticationError as e:
            abort(403)

    return wrapper_func


class CAUser:
    def __init__(self, gmail):
        self.gmail = gmail
        self.pri_key = None
        self.pub_key = None
        self.cert = None
        self.app = Flask(self.gmail)

    @property
    def public_key_object(self):
        return serialization.load_pem_public_key(
            self.pub_key.encode('utf-8'),
            backend=backend
        )

    @property
    def private_key_object(self):
        return serialization.load_pem_private_key(
            self.pri_key.encode('utf-8'),
            backend=backend,
            password=None
        )

    def create_keys_and_get_cert(self):

        self._generate_keys()
        self.send_initial()
        self.app.add_url_rule("/receive_code/",
                              endpoint="/receive_code/", view_func=self.receive_code,
                              methods=["POST"])
        self.app.add_url_rule("/receive_cert/",
                              endpoint="/receive_cert/", view_func=self.receive_cert,
                              methods=["POST"])

    def _generate_keys(self):
        # create a key pair
        k = crypto.PKey()
        k.generate_key(crypto.TYPE_RSA, 1024)

        self.pri_key = crypto.dump_privatekey(crypto.FILETYPE_PEM, k).decode("utf-8")
        self.pub_key = crypto.dump_publickey(crypto.FILETYPE_PEM, k).decode("utf-8")

    def send_initial(self):
        ca_url = SharedData.sections_url_address[SharedData.Entities.CA]
        ca_gmail = SharedData.sections_gmail[SharedData.Entities.CA]

        data = {"gmail": self.gmail, "user_public_key": self.pub_key}
        requests.post(ca_url, json=data)

    def receive_code(self, data):
        ver = data['verification']
        decrypted = self.private_key_object.decrypt(
            ver.encode('utf-8'),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        ca_url = SharedData.sections_url_address[SharedData.Entities.CA]
        ca_gmail = SharedData.sections_gmail[SharedData.Entities.CA]

        requests.post(ca_url, json={"verification": decrypted})

    def receive_cert(self, data):
        cert = data['cert']
        self.cert = cert

    def _add_auth(self, data, receiver_id, timeout=20):
        t0 = datetime.datetime.utcnow()
        delta = datetime.timedelta(seconds=timeout)
        t1 = t0 + delta
        print(receiver_id)
        dictionary = {
            "pubkey": self.pub_key,
            "start_time": datetime.datetime.strftime(t0, TIME_FORMAT),
            "end_time": datetime.datetime.strftime(t1, TIME_FORMAT),
            "sender": self.gmail,
            "receiver": receiver_id,
        }
        pub_sign = sign(self.pri_key, dictionary)
        return {
            "token": {
                "certificate": self.cert,
                "conn_data": dictionary,
                "conn_sign": pub_sign,
            },
            "data": data,
        }

    def remove_auth(self, data):
        try:
            token = data["token"]
            sender_pubkey = token["conn_data"]["pubkey"]
            auth_data = token["conn_data"]
            check_sign(sign_value=token["conn_sign"], data=auth_data, signer_pubkey=sender_pubkey)
            t0, t1 = datetime.datetime.strptime(auth_data["start_time"], TIME_FORMAT), \
                     datetime.datetime.strptime(auth_data["end_time"], TIME_FORMAT)
            now = datetime.datetime.strptime(datetime.datetime.strftime(datetime.datetime.utcnow(), TIME_FORMAT),
                                             TIME_FORMAT)
            if not (t1 >= now >= t0) or (auth_data["receiver"] != self.gmail):
                raise Exception("token invalid")
            check_sign(sign_value=token["certificate"], signer_pubkey="<capubkey>",
                       data={"id": auth_data['sender'], 'pubkey': auth_data['pubkey']})  # TODO
            return data["data"], token["conn_data"]["sender"]
        except Exception as e:
            print(e)
            raise AuthenticationError()

    def send_request(self, url, receiver_id, data, method="post"):
        sender_func = requests.get
        if method.lower() == "post":
            sender_func = requests.post
        authenticated_data = self._add_auth(data, receiver_id)
        response = sender_func(url, json=authenticated_data, verify=True)
        if response.status_code == 200:
            print(response.content)
            return self.remove_auth(json.loads(response.content))
        return response

    def run(self, port):
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        # context.load_cert_chain(self.cert, self.pri_key)
        self.app.run(host='127.0.0.1', port=port, debug=True, )

    @server_auth
    def test(self, data, receiver_id):
        return {"salam": data, "receiver": receiver_id}

    def add_endpoint(self, func, endpoint=None, endpoint_name=None):
        self.app.add_url_rule(endpoint, endpoint_name, func, methods=["GET", "POST"])
