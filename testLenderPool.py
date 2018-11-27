import unittest
from unittest import TestCase
from lenderPool import LenderPool


class LenderPoolTest(TestCase):

    def setUp(self):
        self.lenderPool = LenderPool()
        filename = 'market.csv'
        self.lenderPool.read_lenders(filename)

    def test_read_lenders(self):
        # Input parameters:
        # filename market.csv, ensure that all rows are read
        self.assertEqual(7, len(self.lenderPool.available_lenders))

    def test_choose_lenders_amount_fits_various_lenders(self):
        # Input parameters: Requested amount to borrow is 2000 GPB
        # The first lender is Jane with 480 GPB
        sum_year, sum_month = self.lenderPool.choose_lenders(2000)
        self.assertAlmostEqual(float(2232.4299391), sum_year, delta=1e-07)
        self.assertAlmostEqual(float(62.0119427), sum_month, delta=1e-07)

    def test_choose_lenders_amount_fits_exactly_first_lender(self):
        # Input parameters: Requested amount to borrow is 480 GPB
        # The first lender is Jane with 480 GPB
        sum_year, sum_month = self.lenderPool.choose_lenders(480)
        self.assertAlmostEqual(float(532.7665201), sum_year, delta=1e-07)
        self.assertAlmostEqual(float(14.7990700), sum_month, delta=1e-07)

    def test_choose_lenders_amount_smaller_than_first_lender(self):
        # Input parameters: Requested amount to borrow is 400 GPB
        # The first lender is Jane with 480 GPB
        sum_year, sum_month = self.lenderPool.choose_lenders(400)
        self.assertAlmostEqual(float(443.9721001), sum_year, delta=1e-07)
        self.assertAlmostEqual(float(12.3325583), sum_month, delta=1e-07)


if __name__ == '__main__':
    unittest.main()
