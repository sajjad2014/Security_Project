from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

from src.bank_user import BankUser
from src.shared_data import SharedData


class User(BankUser):
    def __init__(self, gmail):
        super(User, self).__init__(gmail)
        self.create_keys_and_get_cert()
        self.register_and_set_pub_for_bank()

    def send_delegation_rule(self):
        block_chain_url = SharedData.sections_url_address[SharedData.Entities.BlockChain]
        block_chain_gmail = SharedData.sections_gmail[SharedData.Entities.BlockChain]
        # TODO policy
        policy = {"range": 100, "count": 10, "time": "", "type": "USDT"}

        bank_pub_key = self.bank_pub_key

        sign = self.private_key_object.sign(
            {"bank_pub_key": bank_pub_key, "policy": policy},
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        self.send_request(block_chain_url, block_chain_gmail,
                          {"bank_pub_key": bank_pub_key, "user_pub_key": self.pub_key, "policy": policy, "sign": sign})

    def confirm_policy(self, user_pub_key, policy):
        # TODO: what should happen here? nothing
        pass

    def send_buy_item_request(self, item):
        merchant_url = SharedData.sections_url_address[SharedData.Entities.Merchant]
        merchant_gmail = SharedData.sections_gmail[SharedData.Entities.Merchant]
        self.send_request(merchant_url, merchant_gmail, {"user_id": self.gmail, "item": item})

    def incoming_buy_item_price(self, merchant_account_number, item, price, time_stamp):
        pass

    def authenticate_payment(self, merchant_account_number, price):
        bank_url = SharedData.sections_url_address[SharedData.Entities.Bank]
        bank_gmail = SharedData.sections_gmail[SharedData.Entities.Bank]
        self.send_request(bank_url, bank_gmail,
                          {"user_bank_id": self.bank_account_number, "password": self.bank_password,
                           "merchant_bank_id": merchant_account_number, "price": price, })

    def incoming_authenticate_success(self, account_number, merchant_account_number, price):
        # TODO
        pass

    def incoming_confirm_exchange(self, merchant_account_number, user_id, item, price):
        # TODO
        pass
