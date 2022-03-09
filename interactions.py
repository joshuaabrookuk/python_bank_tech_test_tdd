from printtransactions import PrintTransactions

class Interactions(PrintTransactions):

    def deposit(self, ammount):
        self.balance += ammount
        ammount = (format(ammount, '.2f'))
        balance_converted = format(self.balance, '.2f')
        self.transation_list.append(f'{self.date} || {ammount} || || {balance_converted} \n')

    def withdrawal(self, ammount):
        self.balance -= ammount
