from printtransactions import PrintTransactions

class Interactions(PrintTransactions):

    def deposit(self, ammount):
        self.balance += ammount

    def withdrawal(self, ammount):
        self.balance -= ammount

    def print_statment(self):
        return self.header
