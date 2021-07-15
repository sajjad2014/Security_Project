from src.User.user import User

if __name__ == '__main__':
    user: User = User("user@gmail.com")
    # register bank
    user.register_and_set_pub_for_bank()

    # step 1 delegation
    response = user.send_delegation_rule()
    user.confirm_policy(response['user_pub_key'], response['policy'])

    # buy item request
    response = user.send_buy_item_request()
    user.incoming_buy_item_price(response['merchant_account_number'], response['item'], response['price'],
                                 response['time_stamp'])

    # authenticate payment
    # TODO
    # response = user.authenticate_payment()
    # user.incoming_authenticate_success()

    # user.incoming_confirm_exchange()
