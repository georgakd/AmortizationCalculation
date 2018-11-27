"""
This is the main.py script. Input arguments to the script are given via argparse.
The input loan amount is checked to be between the specified range [1000, 15000]
"""

import argparse
import lenderPool


def main():
    parser = argparse.ArgumentParser(description='Loan Calculator')
    parser.add_argument('filename', help='Pool of lenders')
    parser.add_argument('loan_amount', type=int,
                        help='Pick a loan amount of any GBP100 increment between GBP1000 and GBP15000 inclusive')
    args = parser.parse_args()
    source = args.filename

    requested_loan = args.loan_amount

    if not isinstance(requested_loan, int):
        print('Try again with integer amount')
        raise SystemExit

    if (requested_loan < 1000) or (requested_loan > 15000) or (requested_loan % 100 != 0):
        print('Try again with amount between [1000, 15000] in increments of 100')
        raise SystemExit

    # Pool of lenders manipulation
    pool = lenderPool.LenderPool()
    pool.read_lenders(source)
    pool.sort_lenders()
    pool.choose_lenders(requested_loan)


if __name__ == '__main__':
    main()
