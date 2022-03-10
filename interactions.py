from printtransactions import PrintTransactions


class Interactions(PrintTransactions):

    def deposit(self, ammount):
        self.balance += ammount
        ammount = self.__decimalise(ammount)
        balance_converted = self.__decimalise(self.balance)
        self.__adding_one_transaction(ammount, balance_converted)

    def withdrawal(self, ammount):
        self.balance -= ammount

    def __decimalise(self, number):
        return format(number, '.2f')

    def __adding_one_transaction(self, ammount, balance_converted):
        return self.transation_list.append(f'{self.date} || {ammount} || || {balance_converted} \n')
