import unittest
from unittest import TestCase
from amortCalculator import AmortCalculator


class AmortCalculatorTest(TestCase):

    def setUp(self):
        # Input parameters:
        # Rate = 6.9%, Amount to borrow = 480 gbp, years for the loan = 3
        self.calculator = AmortCalculator(0.069, 480, 3)

    def test_monthly_repayment(self):
        result = self.calculator.monthly_repayment()
        self.assertAlmostEqual(float(14.7990700), result, delta=1e-07)

    def test_total_repayment(self):
        result2 = self.calculator.total_repayment()
        self.assertAlmostEqual(float(532.7665201), result2, delta=1e-07)

    def test_annual_interest_rate(self):
        # Input parameters:
        # Summed monthly payment over 36 months 62.0119427, Amount to borrow 2000 gbp
        result = self.calculator.annual_interest_rate(float(62.0119427), 2000)
        self.assertAlmostEqual(float(7.5295052), result, delta=1e-07)


if __name__ == '__main__':
    unittest.main()
