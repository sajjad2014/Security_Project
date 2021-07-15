import datetime

import requests
from OpenSSL import crypto
from cryptography.hazmat.backends.openssl.backend import backend
from cryptography.hazmat.primitives import serialization


class AuthenticationError(Exception):
    pass


def sign(key, data):
    # TODO
    return "signed-string"


def check_sign(sign_value, signer_pubkey, data):
    # TODO
    return True


class CAUser:
    def __init__(self, gmail):
        self.gmail = gmail
        self.pri_key = None
        self.pub_key = None
        self.cert = None

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
        self._get_certificate_from_ca()

    def _generate_keys(self):
        # create a key pair
        k = crypto.PKey()
        k.generate_key(crypto.TYPE_RSA, 1024)

        self.pri_key = crypto.dump_privatekey(crypto.FILETYPE_PEM, k).decode("utf-8")
        self.pub_key = crypto.dump_publickey(crypto.FILETYPE_PEM, k).decode("utf-8")

    def _get_certificate_from_ca(self):
        # TODO
        pass

    def add_auth(self, data, receiver_id, timeout=20):
        t0 = datetime.datetime.utcnow()
        delta = datetime.timedelta(seconds=timeout)
        t1 = t0 + delta
        dictionary = {
            "pubkey": self.pub_key,
            "start_time": str(t0),
            "end_time": str(t1),
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
            t0, t1 = auth_data["t0"], auth_data["t1"]
            now = datetime.datetime.utcnow()
            if not (t1 > now > t0) or not (auth_data["receiver"] != self.gmail):
                raise AuthenticationError()
            check_sign(sign_value=token["certificate"], signer_pubkey="<capubkey>",
                       data={"id": auth_data['sender'], 'pubkey': auth_data['pubkey']})  # TODO
            return data["data"]
        except Exception as e:
            raise AuthenticationError()

    def server_auth(self, func):
        def wrapper_func():
            from flask import request, abort, jsonify
            data = {}
            try:
                data = request.get_json()
            except Exception as e:
                abort(400)
            try:
                return jsonify(func(self.remove_auth(data)))
            except AuthenticationError as e:
                abort(403)

        return wrapper_func

    def send_request(self, url, receiver_id, data, method="post"):
        sender_func = requests.get
        if method.lower() == "post":
            sender_func = requests.post
        authenticated_data = self.add_auth(data, receiver_id)
        sender_func(url, json=authenticated_data, verify=True)

    def public_key_object(self, pub_key):
        return serialization.load_pem_public_key(
            pub_key.encode('utf-8'),
            backend=backend
        )

    def private_key_object(self, pri_key):
        return serialization.load_pem_private_key(
            pri_key.encode('utf-8'),
            backend=backend,
            password=None
        )
