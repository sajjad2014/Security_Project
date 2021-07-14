from OpenSSL import crypto


class CAUser:
    def __init__(self, gmail):
        self.gmail = gmail
        self._pri_key = None
        self._pub_key = None
        self._cert = None

    def create_keys_and_get_cert(self):
        self._generate_keys()
        self._get_certificate_from_ca()

    def _generate_keys(self):
        # create a key pair
        k = crypto.PKey()
        k.generate_key(crypto.TYPE_RSA, 1024)

        self._pri_key = crypto.dump_privatekey(crypto.FILETYPE_PEM, k).decode("utf-8")
        self._pub_key = crypto.dump_publickey(crypto.FILETYPE_PEM, k).decode("utf-8")

    def _get_certificate_from_ca(self):
        # TODO
        pass
