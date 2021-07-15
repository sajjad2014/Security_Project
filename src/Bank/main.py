from src.Bank.bank import Bank
from src.shared_data import SharedData

if __name__ == '__main__':
    bank: Bank = Bank("fgh")
    bank.add_endpoint(bank.incoming_confirm_exchange_from_block_chain, "/incoming_confirm_exchange_from_block_chain/",
                      "incoming_confirm_exchange_from_block_chain")
    bank.add_endpoint(bank.authenticate_payment, "/authenticate_payment/", "authenticate_payment")
    bank.run(SharedData.sections_port_address[SharedData.Entities.Bank])
