from src.Merchant.merchant import Merchant
from src.shared_data import SharedData

if __name__ == '__main__':
    merchant: Merchant = Merchant("", {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5})
    merchant.add_endpoint(merchant.buy_item_request, "/buy_item_request/", "buy_item_request")
    merchant.add_endpoint(merchant.incoming_confirm_exchange, "/incoming_confirm_exchange/",
                          "incoming_confirm_exchange")
    merchant.run(SharedData.sections_port_address[SharedData.Entities.Merchant])
