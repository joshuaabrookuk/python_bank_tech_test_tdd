import unittest
from bank import Bank
from datetime import datetime
now = datetime.now()


class BankTests(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()

    def test_bank_banance(self):
        self.assertEqual(self.bank.balance, 0)


class InteractionsTests(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()

    def test_bank_deposit(self):
        self.bank.deposit(1000)
        self.assertEqual(self.bank.balance, 1000)

    def test_bank_further_deposite(self):
        self.bank.deposit(1000)
        self.bank.deposit(2000)
        self.assertEqual(self.bank.balance, 3000)

    def test_bank_withdrawal(self):
        self.bank.deposit(3000)
        self.bank.withdrawal(500)
        self.assertEqual(self.bank.balance, 2500)


class PrintTransactionsTests(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()
        self.date_today = now.strftime('%m/%d/%Y')

    def test_that_transation_list_is_empty(self):
        self.assertEqual(self.bank.transation_list, [])

    def test_bank_print_adds_header(self):
        self.bank.print_statment()
        self.assertEqual(self.bank.transation_list[0], 'date || credit || debit || balance \n')

    def test_bank_print_prints_header(self):
        self.assertEqual(self.bank.print_statment(), ['date || credit || debit || balance \n'])

    def test_bank_print_first_transaction(self):
        self.bank.deposit(1000)
        self.assertEqual(self.bank.transation_list[0], f'{self.date_today} || 1000.00 || || 1000.00 \n')

    def test_bank_print_first_transaction(self):
        self.bank.deposit(1000)
        self.assertEqual(self.bank.print_statment(), ['date || credit || debit || balance \n',f'{self.date_today} || 1000.00 || || 1000.00 \n'])

    def test_bank_print_second_transaction(self):
        self.bank.deposit(1000)
        self.bank.deposit(2000)
        self.assertEqual(self.bank.transation_list[1], f'{self.date_today} || 2000.00 || || 3000.00 \n')

    def test_bank_print_second_transaction(self):
         self.bank.deposit(1000)
         self.bank.deposit(2000)
         self.assertEqual(self.bank.print_statment(), ['date || credit || debit || balance \n',f'{self.date_today} || 1000.00 || || 1000.00 \n',f'{self.date_today} || 2000.00 || || 3000.00 \n'])

# class PrivateClassTests(unittest.TestCase):
#
#     def setUp(self):
#         self.bank = Bank()
#
#     def test_private_decimalise_method(self):
#         self.assertEqual(self.bank.__decimalise(10), 10.00)

if __name__ == '__main__':
    unittest.main()
