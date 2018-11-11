from calculator import Calculator
from decimal import Decimal
import numpy as np


class CompoundInterestCalculator(Calculator):
    def __init__(self, rate, requested_amount, years):
        self.rate = Decimal(rate)
        self.requested_amount = Decimal(requested_amount)
        self.years = years

    def monthly_repayment(self):
        """
        https://www.vertex42.com/ExcelArticles/amortization-calculation.html
        The formula for calculating the payment amount is shown below.

        A = P*(r(1 + r)**n) / ((1+r)**n - 1)

        Where:
        A = payment Amount per period
        P = initial Principal (loan amount)
        r = interest rate per period, for annual rate we have r / 12 months
        n = total number of payments or periods, in our case 3*12 = 36 periods
        """
        rate_per_period = Decimal(self.rate/12)
        expo = Decimal((1+rate_per_period)**(self.years*12))
        result = Decimal(self.requested_amount*rate_per_period*expo/(expo-1))
        return result

    def total_repayment(self):
        result = Decimal(self.monthly_repayment()*self.years*12)
        return result

    def combined_lenders_repayment(self):
        total_repayment = self.total_repayment()
        monthly_repayment = self.monthly_repayment()

        return total_repayment, monthly_repayment

    def annual_interest_rate(self, monthly_payment, requested_loan):
        """
        https://www.vertex42.com/ExcelArticles/amortization-calculation.html
        The formula for calculating the annual interest rate is shown below.

        i = n*((r+1)**(p/n)-1)

        Where:
        i = annual interest rate
        n = 1 for annual compound period
        p = number of payment periods per year
        r is the function call of np.rate
        """

        annual_rate = Decimal(((np.rate(12 * self.years, -monthly_payment, requested_loan, 0) + 1)**12 - 1) * 100)
        return annual_rate
