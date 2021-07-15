from src.CA.CA_model import CA
from src.shared_data import SharedData

if __name__ == '__main__':
    bank: CA = CA()
    bank.add_endpoint(bank.authenticate_payment, "/authenticate_payment/", "authenticate_payment")
    bank.run(SharedData.sections_port_address[SharedData.Entities.CA])
