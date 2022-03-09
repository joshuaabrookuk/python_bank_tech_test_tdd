from datetime import datetime
now = datetime.now()


class PrintTransactions(object):

    def __init__(self):
        self.header = 'date || credit || debit || balance \n'
        self.transation_list = []
        self.date = now.strftime('%m/%d/%Y')

    def print_statment(self):
        self.transation_list.insert(0, self.header)
        return self.transation_list
