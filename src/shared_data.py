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

    sections_url_address = {Entities.CA: "localhost:4000", Entities.Bank: "localhost:4001",
                            Entities.User: "localhost:4002",
                            Entities.BlockChain: "localhost:4003",
                            Entities.Merchant: "localhost:4004", Entities.ExchangeCenter: "localhost:4005"}

    sections_port_address = {Entities.CA: 4000, Entities.Bank: 4001, Entities.User: 4002,
                             Entities.BlockChain: 4003,
                             Entities.Merchant: 4004, Entities.ExchangeCenter: 4005}

    CA_PUBLIC_KEY = ""  # TODO: TO BE SET LATER
