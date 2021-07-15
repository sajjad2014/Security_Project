class CryptoAccount:
    def __init__(self, pub_key, wallet):
        self.pub_key = pub_key
        self.wallet = wallet #map of all crypto types and their amounts
        self.policy = {}

    def increase(self, type, amount):
        if type in self.wallet:
            self.wallet[type] += amount
        else:
            self.wallet[type] = amount
        return True

    def reduce(self, type, amount):
        if type in self.wallet:
            if self.wallet[type] > amount:
                self.wallet -= amount
                return True
        return False

    def add_policy(self, bank_pub_key, policy):
        self.policy[bank_pub_key] = policy

    def verify_policy(self, bank_pub_key):
        if bank_pub_key in self.policy:
            return self.policy[bank_pub_key]

    def use_policy(self, bank_pub_key, amount):
        self.policy[bank_pub_key]["range"] -= amount
        self.policy[bank_pub_key]["count"] -= 1
