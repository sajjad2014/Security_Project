from src.CA_user import CAUser
from src.shared_data import SharedData


class BankUser(CAUser):
    def __init__(self, gmail):
        super(BankUser, self).__init__(gmail)

        self.bank_account_number = None
        self.bank_password = None
        self.bank_pub_key = None

    def register_and_set_pub_for_bank(self):
        self._register_to_bank()
        self._set_pub_key_in_bank()

    def _register_to_bank(self):
        bank_url = SharedData.sections_url_address[SharedData.Entities.Bank]
        bank_gmail = SharedData.sections_gmail[SharedData.Entities.Bank]
        self.send_request(bank_url, bank_gmail, {"user_id": self.gmail})

    def _set_pub_key_in_bank(self):
        bank_url = SharedData.sections_url_address[SharedData.Entities.Bank]
        bank_gmail = SharedData.sections_gmail[SharedData.Entities.Bank]
        self.send_request(bank_url, bank_gmail, {"user_id": self.gmail, "user_pub_key": self.pub_key,
                                                 "user_bank_id": self.bank_account_number,
                                                 "password": self.bank_password, "user_certificate": self.cert})
