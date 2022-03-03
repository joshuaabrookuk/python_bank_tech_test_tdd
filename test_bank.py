import unittest
from bank import Bank

class BankTests(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()

    def test_bank_banance(self):
        self.assertEqual(self.bank.balance, 0)

    def test_bank_deposit(self):
        self.bank.credit(1000)
        self.assertEqual(self.bank.balance, 1000)

    def test_bank_further_deposite(self):
        self.bank.credit(1000)
        self.bank.credit(2000)
        self.assertEqual(self.bank.balance, 3000)

if __name__ == '__main__':
    unittest.main()
