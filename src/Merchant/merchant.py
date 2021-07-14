from src.bank_user import BankUser


class Merchant(BankUser):
    def __init__(self, gmail, items_price=None):
        super(Merchant, self).__init__(gmail)
        self.create_keys_and_get_cert()
        self.register_and_set_pub_for_bank()

        self.items_price = items_price if items_price else {}  # key:item_name, value:price
        self._customers_item_request = {}

        # todo set ca_pub_key
        self.ca_pub_key = None

    def buy_item_request(self, user_id, item, time_stamp):
        # TODO new time_stamp ?
        self._customers_item_request[user_id] = item
        return self.bank_account_number, item, self.items_price.get(item, -1), time_stamp

    def send_item_price(self):
        # TODO
        pass

    def incoming_confirm_exchange(self, merchant_bank_id, user_id, price):
        item = self._customers_item_request[user_id]
        if self.items_price.get(item, -1) == price and self.bank_account_number == merchant_bank_id:
            del self._customers_item_request[user_id]
            return True
        return False
