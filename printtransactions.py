from datetime import datetime
now = datetime.now()


class PrintTransactions(object):

    def __init__(self):
        self.header = 'date || credit || debit || balance \n'
        self.transation_list = []
        self.date = now.strftime('%m/%d/%Y')

    def print_statment(self):
        self._remove_header(self.transation_list)
        for e in self.transation_list:
            print(e)
        self.transation_list.insert(0, self.header)
        return self.transation_list

    def _remove_header(self, arg):
        if arg != [] and arg[0] == self.header:
            self.transation_list.pop(0)
        else:
            self.transation_list
