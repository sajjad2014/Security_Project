from src.User.user import User
from src.shared_data import SharedData

if __name__ == '__main__':
    user: User = User(SharedData.sections_gmail[SharedData.Entities.User])

    # # step 1 delegation
    # response = user.send_delegation_rule()
    # user.confirm_policy(response['user_pub_key'], response['policy'])
    #
    # # buy item request
    # response = user.send_buy_item_request("2")
    # user.add_endpoint(user.incoming_buy_item_price, "/incoming_buy_item_price/",
    #                   "incoming_buy_item_price")
    #
    # user.add_endpoint(user.incoming_authenticate_success, "/incoming_authenticate_success/",
    #                   "incoming_authenticate_success")
    # user.add_endpoint(user.incoming_confirm_exchange, "/incoming_confirm_exchange/",
    #                   "incoming_confirm_exchange")
    user.run(port=SharedData.sections_port_address[SharedData.Entities.User])
