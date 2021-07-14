from src.CA_user import CAUser


class BankUser(CAUser):
    def __init__(self, gmail):
        super(BankUser, self).__init__(gmail)

        self.bank_account_number = None
        self.bank_password = None

    def register_and_set_pub_for_bank(self):
        self._register_to_bank()
        self._set_pub_key_in_bank()

    def _register_to_bank(self):
        # todo register to bank using id and get password
        pass

    def _set_pub_key_in_bank(self):
        # todo send credentials to bank to set the public key
        pass
