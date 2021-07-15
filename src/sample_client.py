from CA_user import CAUser

user = CAUser("balam")
user.create_keys_and_get_cert()
print(user.send_request("http://localhost:4000", "salam", "baba").reason)
