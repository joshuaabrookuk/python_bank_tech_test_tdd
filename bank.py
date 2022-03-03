class Bank():

    def __init__(self):
        self.balance = 0

    def deposit(self, ammount):
        self.balance += ammount

    def withdrawal(self, ammount):
        self.balance -= ammount
