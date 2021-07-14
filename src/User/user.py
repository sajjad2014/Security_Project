from src.bank_user import BankUser


class User(BankUser):
    def __init__(self, gmail):
        super(User, self).__init__(gmail)
        self.create_keys_and_get_cert()
        self.register_and_set_pub_for_bank()

        # todo set ca_pub_key
        self.ca_pub_key = None

    def send_delegation_rule(self):
        # todo generate and send delegation rule to blockchain
        pass

    def confirm_policy(self, user_pub_key, policy):
        # TODO: what should happen here? nothing
        pass

    def send_buy_item_request(self):
        # TODO
        pass

    def incoming_buy_item_price(self, merchant_account_number, item, price, time_stamp):
        pass

    def authenticate_payment(self, account_number, bank_password, merchant_account_number, price, time_stamp):
        # todo process this request and send authentication payment to bank
        pass

    def incoming_authenticate_success(self, account_number, merchant_account_number, price):
        # TODO
        pass

    def incoming_confirm_exchange(self, merchant_account_number, user_id, item, price):
        # TODO
        pass
