from CA_user import CAUser

user = CAUser("salam")
user.create_keys_and_get_cert()
user.add_endpoint(user.test, "/", "sth")
user.run(4000)
