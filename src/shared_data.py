class SharedData:
    class Entities:
        Bank = "Bank"
        User = "User"
        BlockChain = "BlockChain"
        Merchant = "Merchant"
        ExchangeCenter = "ExchangeCenter"
        CA = "CA"

    sections_gmail = {Entities.CA: "CA", Entities.Bank: "bank@gmail.com",
                      Entities.User: "user@gmail.com",
                      Entities.BlockChain: "blockchain@gmail.com",
                      Entities.Merchant: "merchant@gmail.com",
                      Entities.ExchangeCenter: "exchange_center@gmail.com"}

    sections_url_address = {Entities.CA: "", Entities.Bank: "", Entities.User: "", Entities.BlockChain: "",
                            Entities.Merchant: "", Entities.ExchangeCenter: ""}

    CA_PUBLIC_KEY = ""  # TODO: TO BE SET LATER
