from transactions import Transactions

class Interactions(Transactions):

    def deposit(self, ammount):
        self.balance += ammount

    def withdrawal(self, ammount):
        self.balance -= ammount

    def print_statment():
        return 'date || credit || debit || balance'
