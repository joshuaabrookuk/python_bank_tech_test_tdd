import unittest
from bank import Bank

class BankTests(unittest.TestCase):

    def test_bank_banance(self):
        bank = Bank()
        self.assertEqual(bank.balance, 0)

    def test_bank_deposit(self):
        bank = Bank()
        bank.credit(1000)
        self.assertEqual(bank.balance, 1000)

if __name__ == '__main__':
    unittest.main()
