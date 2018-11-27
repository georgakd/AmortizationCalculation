"""
This is the Lender class. Each row of the market.csv is a Lender object.
To print the information of each object a display_lender method could be used.
"""


class Lender(object):
    def __init__(self, name, rate, amount):
        self.name = name
        self.rate = float(rate)
        self.amount = float(amount)

    def display_lender(self):
        pass
