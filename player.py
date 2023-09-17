class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def gamble(self, amount):
        if (amount > self.money):
            print(
                f"\ncannot bet ${amount} because your balance is only ${self.money}")
        else:
            self.money -= amount
            print(f"Sorry {self.name} , you have ${self.money} left now")
