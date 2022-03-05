import unittest
from bank import Bank


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


class TransactionsTests(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()

    def test_bank_print_first_line(self):
        first_line = self.bank.print_statment
        self.assertEqual(self.bank.print_statment, first_line)


if __name__ == '__main__':
    unittest.main()
