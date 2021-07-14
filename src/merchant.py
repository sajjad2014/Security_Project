class Merchant:
    def __init__(self):
        self.merch_price_pair = {}
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

    def payment_request(self):
        #todo send price to client
        # I know it sounds stupid but this is first step
        pass

    def verify_payment(self, id_user, pub_user, price, msg):
        if msg == "OK":
            #todo ship merchandise to user /or send user
            # a msg indicating successful transaction
            pass