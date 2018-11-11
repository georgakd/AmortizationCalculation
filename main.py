"""
This is the main.py script. Input arguments to the script are given via argparse.

"""

import argparse
import lenderPool


def main():
    parser = argparse.ArgumentParser(description='Loan Calculator')
    parser.add_argument('filename', help='Pool of lenders')
    parser.add_argument('loan_amount',
                        help='Pick a loan amount of any £100 increment between £1000 and £15000 inclusive')
    args = parser.parse_args()
    source = args.filename

    requested_loan = int(args.loan_amount)
    if (requested_loan < 1000) or (requested_loan > 15000) or (requested_loan % 100 != 0):
        print('Try again with amount between [1000, 15000] in increments of 100')
        raise SystemExit


    # Pool of lenders
    pool = lenderPool.LenderPool()
    pool.read_lenders(source)
    pool.sort_lenders()
    pool.choose_lenders(requested_loan)


if __name__ == '__main__':
    main()
