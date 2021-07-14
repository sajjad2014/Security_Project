class User:
    def __init__(self):
        self.pub_id = None
        self.bank_id = None
        self.bank_pass = None
        # todo set ca_pub_key
        self.ca_pub_key = None
        # todo generate and verify self public and private key
        self.pub_key = None
        self.pri_key = None

    def register_to_bank(self):
        #todo register to bank using id and get password
        pass

    def set_pub_key_in_bank(self):
        #todo send credentials to bank to set the public key
        pass

    def send_delegation_rule(self):
        #todo generate and send delegation rule to blockchain
        pass

    def get_payment_request(self, price, id_merchant, timestamp):
        #todo process this request and send authentication payment to bank
        pass

