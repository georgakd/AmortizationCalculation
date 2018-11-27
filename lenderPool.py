"""
This is the LenderPool class. It stores a pool of available lenders.
After the lenders are sorted, the algorithm uses the amount and rate
of each lender to eventually cover the total amount asked to borrow.
"""


from lender import Lender
from amortCalculator import AmortCalculator
import csv


# For back compatibility with python 2.x
# ***************************************
try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError
# ***************************************


class LenderPool(object):
    def __init__(self):
        # construct available lender object list
        self.available_lenders = []

    def read_lenders(self, source):
        try:
            with open(source, 'r') as file:
                reader = csv.reader(file)
                lenders = list(reader)
                lenders.pop(0)  # remove header

            for index in lenders:
                lender = Lender(index[0], float(index[1]), float(index[2]))
                self.available_lenders.append(lender)

        except FileNotFoundError:
            print('File does not exist...Try again...')
            raise SystemExit

    def sort_lenders(self):
        # To return a new sorted list
        return sorted(self.available_lenders, key=lambda x: x.rate)

    def display_results_over_lenders(self, amount, rate, month_pay, total_pay):
        print(u"Requested amount: \u00A3{0:4d}".format(amount))
        print(u"Rate: {0:3.1f}%".format(rate))
        print(u"Monthly repayment: \u00A3{0:5.2f}".format(month_pay))
        print(u"Total repayment: \u00A3{0:7.2f}".format(total_pay))

    def sums_over_lenders(self, loan_calculator, sum_year, sum_month):
        total_repayment, monthly_repayment = loan_calculator.combined_lenders_repayment()
        sum_year += total_repayment
        sum_month += monthly_repayment
        return sum_year, sum_month

    def choose_lenders(self, requested_amount):

        sorted_lenders_list = self.sort_lenders()
        requested_amount_from_borrower = requested_amount
        all_lender_amounts = 0
        for element in sorted_lenders_list:
            all_lender_amounts += element.amount

        if requested_amount > all_lender_amounts:
            print('Not possible to provide a quote right now.')
            raise SystemExit

        loan_years = 3  # or 36 months
        sum_year = sum_month = 0
        counter = 0
        for element in sorted_lenders_list:
            counter += 1
            requested_amount = requested_amount - element.amount

            if requested_amount > 0:  # keep looping over the borrowers
                loan_calculator = AmortCalculator(element.rate, element.amount, loan_years)
                sum_year, sum_month = self.sums_over_lenders(loan_calculator, sum_year, sum_month)
                annual_rate = loan_calculator.annual_interest_rate(sum_month, requested_amount_from_borrower)

            if requested_amount == 0:  # the amount fits perfectly in the first borrower
                loan_calculator = AmortCalculator(element.rate, element.amount, loan_years)
                sum_year, sum_month = self.sums_over_lenders(loan_calculator, sum_year, sum_month)
                annual_rate = loan_calculator.annual_interest_rate(sum_month, requested_amount_from_borrower)
                break

            if requested_amount < 0 and counter == 1:  # requested amount_smaller_than_first_lender
                loan_calculator = AmortCalculator(element.rate, requested_amount_from_borrower, loan_years)
                sum_year, sum_month = self.sums_over_lenders(loan_calculator, sum_year, sum_month)
                annual_rate = loan_calculator.annual_interest_rate(sum_month, requested_amount_from_borrower)
                break

            if requested_amount < 0 and counter != 1:
                loan_calculator = AmortCalculator(element.rate, abs(requested_amount+element.amount), loan_years)
                sum_year, sum_month = self.sums_over_lenders(loan_calculator, sum_year, sum_month)
                annual_rate = loan_calculator.annual_interest_rate(sum_month, requested_amount_from_borrower)
                break

        self.display_results_over_lenders(requested_amount_from_borrower, annual_rate, sum_month, sum_year)

        return sum_year, sum_month
