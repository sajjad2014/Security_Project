import random

from src.CA_user import CAUser


class BankUserDataModel:
    def __init__(self, gmail, account_number, password):
        self.gmail: str = gmail
        self.account_number: str = account_number
        self.password: str = password


class Bank(CAUser):
    last_created_account = 100000

    @classmethod
    def generate_password(cls) -> str:
        return str(random.randint(100000, 999999))

    @classmethod
    def generate_new_account_number(cls) -> str:
        cls.last_created_account += 1
        return str(cls.last_created_account)

    def __init__(self, gmail):
        sup = super().__init__(gmail)
        sup.create_keys_and_get_cert()

        # todo set ca_pub_key
        self.ca_pub_key = None

        self.users_data = {}
        self.delegations = []

    def register(self, id):
        # todo generate a password and return it
        pass

    def register_pub_key(self, gmail, account_number, password, pub_key, cert):
        # if bank_id in self.user_pass_pair:
        #     if self.user_pass_pair[bank_id] == password:
        #         # todo check pub_id and pub_key in cert and return ok if we good
        #         pass
        # # else return not ok
        pass

    def authenticate_payment(self, bank_id, password, price, pub_key):
        if bank_id in self.user_pass_pair:
            if self.user_pass_pair[bank_id] == password:
                # todo check pub_key maybe?
                # todo send a request to blockchain for delegation
                pass

    def finalize_delegation(self, pub_user, price, res):
        if res == "OK":
            # todo find related delegation block and
            # transfer amount to id_merchant
            # and send success message to merchant
            pass

    def physical_registration(self, gmail):
        password = self.generate_password()
        account_number = self.generate_new_account_number()
        bank_user_data = BankUserDataModel(gmail, account_number, password)
        self.users_data[gmail] = bank_user_data
        return password, account_number
