import unittest
from bank import Bank

class BankTests(unittest.TestCase):

    def test_bank_deposit(self):
        bank = Bank()
        self.assertEqual(bank.balance, 0)

if __name__ == '__main__':
    unittest.main()
