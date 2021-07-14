class Bank:
    def __init__(self):
        self.user_pass_pair = {}
        self.user_pub_info = {} #I think it should include pub_id, pub_key and cert and
        self.delegations = []
        #todo set ca_pub_key
        self.ca_pub_key = None
        # todo generate and verify self public and private key
        self.pub_key = None
        self.pri_key = None

    def register(self, id):
        #todo generate a password and return it
        pass

    def register_pub_key(self, bank_id, password, pub_id, pub_key, cert):
        if bank_id in self.user_pass_pair:
            if self.user_pass_pair[bank_id] == password:
                #todo check pub_id and pub_key in cert and return ok if we good
                pass
        #else return not ok

    def authenticate_payment(self, bank_id, password, price, pub_key):
        if bank_id in self.user_pass_pair:
            if self.user_pass_pair[bank_id] == password:
                #todo check pub_key maybe?
                #todo send a request to blockchain for delegation
                pass

    def finalize_delegation(self, pub_user, price, res):
        if res == "OK":
            #todo find related delegation block and
            # transfer amount to id_merchant
            # and send success message to merchant
            pass