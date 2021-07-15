import random

from src.CA_user import CAUser, server_auth
from src.shared_data import SharedData


class BankUserDataModel:
    def __init__(self, gmail, account_number, password):
        self.gmail: str = gmail
        self.account_number: str = account_number
        self.password: str = password
        self.public_key = None
        self.credit = 0
        self.in_process_exchange = []  # (dest account number, price)


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
        super(Bank, self).__init__(gmail)
        self.create_keys_and_get_cert()

        self._users_data = {}
        self._delegations = []

    def _get_user_data_model_by_pub_key(self, user_pub_key):
        for gmail in self._users_data.keys():
            if self._users_data[gmail].public_key == user_pub_key:
                return self._users_data[gmail]
        return None

    def _get_user_data_model_by_account_number(self, account_number):
        for gmail in self._users_data.keys():
            if self._users_data[gmail].account_number == account_number:
                return self._users_data[gmail]
        return None

    def physical_registration(self, gmail):
        password = self.generate_password()
        account_number = self.generate_new_account_number()
        bank_user_data = BankUserDataModel(gmail, account_number, password)
        self._users_data[gmail] = bank_user_data
        return password, account_number

    def register_pub_key(self, gmail, account_number, password, pub_key):
        bank_user_data: BankUserDataModel = self._users_data.get(gmail, None)
        if bank_user_data:
            if bank_user_data.account_number == account_number and bank_user_data.password == password:
                bank_user_data.public_key = pub_key
                return {"status": "OK", "bank_pub_key": self.pub_key}
        return {}

    @server_auth
    def authenticate_payment(self, gmail, account_number, password, merchant_account_number, price, time_stamp):
        bank_user_data: BankUserDataModel = self._users_data.get(gmail, None)
        if bank_user_data:
            if bank_user_data.account_number == account_number and bank_user_data.password == password:
                bank_user_data.in_process_exchange.append((merchant_account_number, price))
                return account_number, merchant_account_number, price
        return "provided informations does not match"

    def send_exchange_crypto(self, user_pub_key, price):
        block_chain_url = SharedData.sections_url_address[SharedData.Entities.BlockChain]
        block_chain_gmail = SharedData.sections_gmail[SharedData.Entities.BlockChain]
        self.send_request(block_chain_url, block_chain_gmail,
                          {"user_pub_key": user_pub_key, "bank_pub_key": self.pub_key, "price": price})

    @server_auth
    def incoming_confirm_exchange_from_block_chain(self, user_pub_key, price):
        user_data_model: BankUserDataModel = self._get_user_data_model_by_pub_key(user_pub_key)
        if user_data_model:
            for in_process in user_data_model.in_process_exchange:
                if in_process[1] == price:
                    user_data_model.in_process_exchange.remove(in_process)
                    dest_user_data_model: BankUserDataModel = self._get_user_data_model_by_account_number(in_process[0])
                    dest_user_data_model.credit += price
                    break
        return False

    def send_confirm_exchange_to_merchant(self, merchant_account_number, user_id, price):
        merchant_url = SharedData.sections_url_address[SharedData.Entities.Merchant]
        merchant_gmail = SharedData.sections_gmail[SharedData.Entities.Merchant]
        self.send_request(merchant_url, merchant_gmail,
                          {"merchant_bank_id": merchant_account_number, "user_id": user_id, "price": price})
