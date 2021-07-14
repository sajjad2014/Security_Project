class ExchangeCenter:
    def __init__(self):
        self.map_crypto_to_doller = {}
        # todo set ca_pub_key
        self.ca_pub_key = None
        # todo generate and verify self public and private key
        self.pub_key = None
        self.pri_key = None

    def price(self, crypto_type, amount):
        if crypto_type in self.map_crypto_to_doller:
            return amount * self.map_crypto_to_doller[crypto_type]

    def AsyncExchange(self, receiver_account, wallet_address, crypto_type, doller_amount, signature, timestamp):
        #todo check signature and account value if everything is good
        # send a message to bank/blockchain to show the successful operation
        pass
