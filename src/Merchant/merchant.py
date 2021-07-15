from src.CA_user import server_auth
from src.bank_user import BankUser
from src.shared_data import SharedData


class Merchant(BankUser):
    def __init__(self, gmail, items_price=None):
        super(Merchant, self).__init__(gmail)
        self.create_keys_and_get_cert()
        self.register_and_set_pub_for_bank()

        self.items_price = items_price if items_price else {}  # key:item_name, value:price
        self._customers_item_request = {}

    @server_auth
    def buy_item_request(self, user_id, item):
        self._customers_item_request[user_id] = item
        return self.bank_account_number, item, self.items_price.get(item, -1)

    def send_item_price(self, user_id, item, price):
        c_url = SharedData.sections_url_address[SharedData.Entities.User]
        self.send_request(c_url, user_id, {"merchant_bank_id": self.bank_account_number, "item": item, "price": price})

    @server_auth
    def incoming_confirm_exchange(self, merchant_bank_id, user_id, price):
        item = self._customers_item_request[user_id]
        if self.items_price.get(item, -1) == price and self.bank_account_number == merchant_bank_id:
            del self._customers_item_request[user_id]
            return True
        return False
