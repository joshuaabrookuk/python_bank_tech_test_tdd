from printtransactions import PrintTransactions

class Interactions(PrintTransactions):

    def deposit(self, ammount):
        self.balance += ammount
        self.transation_list.append(f'{self.date} || {ammount} || || {self.balance}')

    def withdrawal(self, ammount):
        self.balance -= ammount
