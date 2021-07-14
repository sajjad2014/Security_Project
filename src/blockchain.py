class BlockChain:
    def __init__(self):
        self.block_list = []
        self.pub_key_crypto_pair = {}
        self.pub_key_delegation_pair = {}
        # todo set ca_pub_key
        self.ca_pub_key = None
        # todo generate and verify self public and private key
        self.pub_key = None
        self.pri_key = None

    def add_new_block(self, data):
        if self.concession(data):
            self.block_list.append(data)

    def concession(self, data):
        #I have no idea what these functions do or how they should work
        pass

    def add_delegation(self, policy, cert, pub_bank, sing_policy, timestamp):
        #todo check certifications and add a new delegation
        pass

    def exchange_crypto(self, pub_user, price, pub_bank, cert, id_merchant, time_stamp):
        #todo check delegation rule then send a message to exchange center to cash in the crypto
        pass

    def confirm_exchange(self, pub_user, price, id_merchant):
        #todo add new block to block list
        # and send a message to bank for conformation or let ExchangeCenter do it
        pass