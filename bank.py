from interactions import Interactions

class Bank(Interactions):

    def __init__(self):
        self.balance = 0
        super(Interactions, self).__init__()
