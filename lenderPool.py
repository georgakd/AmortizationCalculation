from lender import Lender
from compoundInterestCalculator import CompoundInterestCalculator
from decimal import Decimal
import csv


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
                lender = Lender(index[0], Decimal(index[1]), Decimal(index[2]))
                self.available_lenders.append(lender)

        except FileNotFoundError:
            print('File does not exist...Try again...')

    def sort_lenders(self):
        # To return a new sorted list
        return sorted(self.available_lenders, key=lambda x: x.rate)

    def summations_over_lenders(self, requested_amount, amount, rate, years, sum_month, sum_total):
        loan_calculator = CompoundInterestCalculator(rate, amount, years)
        total_repayment, monthly_repayment = loan_calculator.combined_lenders_repayment()

        print(requested_amount, amount, rate, monthly_repayment, total_repayment)

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
                loan_calculator = CompoundInterestCalculator(element.rate, element.amount, loan_years)
                total_repayment, monthly_repayment = loan_calculator.combined_lenders_repayment()
                sum_year += total_repayment
                sum_month += monthly_repayment
                annual_rate = loan_calculator.annual_interest_rate(sum_month, requested_amount_from_borrower)
                print(requested_amount, element.amount, element.rate, monthly_repayment, total_repayment)

            if requested_amount == 0:  # the amount fits perfectly in the first borrower
                loan_calculator = CompoundInterestCalculator(element.rate, element.amount, loan_years)
                total_repayment, monthly_repayment = loan_calculator.combined_lenders_repayment()
                sum_year += total_repayment
                sum_month += monthly_repayment
                print(requested_amount, element.amount, element.rate, monthly_repayment, total_repayment)
                annual_rate = loan_calculator.annual_interest_rate(sum_month, requested_amount_from_borrower)
                break
            if requested_amount < 0 and counter == 1:
                loan_calculator = CompoundInterestCalculator(element.rate, requested_amount_from_borrower, loan_years)
                total_repayment, monthly_repayment = loan_calculator.combined_lenders_repayment()
                sum_year += total_repayment
                sum_month += monthly_repayment
                print(requested_amount, element.amount, element.rate, monthly_repayment, total_repayment)
                annual_rate = loan_calculator.annual_interest_rate(sum_month, requested_amount_from_borrower)
                break
            if requested_amount < 0 and counter != 1:
                loan_calculator = CompoundInterestCalculator(element.rate, abs(requested_amount+element.amount), loan_years)
                total_repayment, monthly_repayment = loan_calculator.combined_lenders_repayment()
                sum_year += total_repayment
                sum_month += monthly_repayment
                print(requested_amount, element.amount, element.rate, monthly_repayment, total_repayment)
                annual_rate = loan_calculator.annual_interest_rate(sum_month, requested_amount_from_borrower)
                break

        print(sum_month, sum_year, annual_rate)
