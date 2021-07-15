class SharedData:
    class Entities:
        Bank = "Bank"
        User = "User"
        BlockChain = "BlockChain"
        Merchant = "Merchant"
        ExchangeCenter = "ExchangeCenter"
        CA = "CA"

    sections_gmail = {Entities.CA: "cagmailcom", Entities.Bank: "bankgmailcom",
                      Entities.User: "usergmailcom",
                      Entities.BlockChain: "blockchaingmailcom",
                      Entities.Merchant: "merchantgmailcom",
                      Entities.ExchangeCenter: "exchangecentergmailcom"}

    sections_url_address = {Entities.CA: "http://localhost:4000", Entities.Bank: "http://localhost:4001",
                            Entities.User: "http://localhost:4002",
                            Entities.BlockChain: "http://localhost:4003",
                            Entities.Merchant: "http://localhost:4004",
                            Entities.ExchangeCenter: "http://localhost:4005"}

    sections_port_address = {Entities.CA: 4000, Entities.Bank: 4001, Entities.User: 4002,
                             Entities.BlockChain: 4003,
                             Entities.Merchant: 4004, Entities.ExchangeCenter: 4005}

    CA_PUBLIC_KEY = ""  # TODO: TO BE SET LATER
