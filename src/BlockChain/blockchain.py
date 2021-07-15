import json

from src.BlockChain.crypto_account import CryptoAccount
from src.CA_user import CAUser
from cryptography.hazmat.backends.openssl.backend import backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding


class BlockChain(CAUser):
    def __init__(self, gmail):
        super().__init__(gmail)
        self.create_keys_and_get_cert()
        self.block_list = []
        self.pub_key_account_pair = {}
        self.map_crypto_to_doller = {}

    def add_new_block(self, data):
        if self.concession(data):
            self.block_list.append(data)

    def concession(self, data):
        # I have no idea what these functions do or how they should work
        pass

    def add_policy(self, data):
        bank_pub_key = data["bank_pub_key"]
        user_pub_key = data["user_pub_key"]
        policy = data["policy"]
        signature = data["signature"]
        if user_pub_key in self.pub_key_account_pair:
            bank_pub_key_obj = self.public_key_object(bank_pub_key)
            unsigned_msg = json.dumps({"bank_pub_key": bank_pub_key,
                                       "policy": policy}).encode('utf-8')
            bank_pub_key_obj.verify(
                signature,
                unsigned_msg,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256())
            account = self.pub_key_account_pair[user_pub_key]
            account.add_policy(policy)
            # todo send bak the response

            return {"user_pub_key": user_pub_key, "policy": policy}

    def crypto_to_dollar(self, crypto_type, amount):
        if crypto_type in self.map_crypto_to_doller:
            return amount * self.map_crypto_to_doller[crypto_type]

    def dollar_to_crypto(self, crypto_type, amount):
        if crypto_type in self.map_crypto_to_doller:
            return amount / self.map_crypto_to_doller[crypto_type]

    def exchange_crypto(self, data):
        user_pub_key = data["user_pub_key"]
        price = data["price"]
        bank_pub_key = data["bank_pub_key"]
        if user_pub_key in self.pub_key_account_pair:
            account: CryptoAccount = self.pub_key_account_pair[user_pub_key]
            policy = account.verify_policy(bank_pub_key)
            policy_type = policy["type"]
            policy_count = policy["count"]
            policy_range = policy["range"]
            crypto_price = self.dollar_to_crypto(policy_type, price)
            #todo check timestame
            if policy_count > 0 and policy_range > crypto_price and policy_type in account.wallet:
                cur_amount = account.wallet[policy_type]
                if cur_amount > crypto_price:
                    account.reduce(policy_type, crypto_price)
                    account.use_policy(bank_pub_key, crypto_price)
                    return {"user_pub_key": user_pub_key,
                            "price": price}
                    #todo send back a response
        # todo check delegation rule then send a message to exchange center to cash in the crypto
        pass

