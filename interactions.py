from printtransactions import PrintTransactions


class Interactions(PrintTransactions):

    def deposit(self, ammount):
        self.balance += ammount
        ammount = self.__decimalise(ammount)
        balance_converted = self.__decimalise(self.balance)
        self.transation_list.append(f'{self.date} || {ammount} || || {balance_converted} \n')

    def withdrawal(self, ammount):
        self.balance -= ammount
        ammount = self.__decimalise(ammount)
        balance_converted = self.__decimalise(self.balance)
        self.transation_list.append(f'{self.date} || || {ammount} || {balance_converted} \n')

    def __decimalise(self, number):
        return format(number, '.2f')

    # def __adding_one_transaction(self, ammount, balance_converted):
    #     if balance_converted > str(self.balance):
    #         return self.transation_list.append(f'{self.date} || {ammount} || || {balance_converted} \n')
    #     else:
    #         return self.transation_list.append(f'{self.date} || || {ammount} || {balance_converted} \n')
