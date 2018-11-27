There is a need for a rate calculation system allowing prospective borrowers to obtain a quote from our pool of lenders for 36 month loans. This system will take the form of a command-line application. You will be provided with a file containing a list of all the offers being made by the lenders within the system in CSV format, see the example market.csv file provided alongside this specification. You should strive to provide as low a rate to the borrower as is possible to ensure that the quotes are as competitive as they can be against competitors'. You should also provide the borrower with the details of the monthly repayment amount and the total repayment amount. Repayment amounts should be displayed to 2 decimal places and the rate of the loan should be displayed to one decimal place. Borrowers should be able to request a loan of any £100 increment between £1000 and £15000 inclusive. If the market does not have sufficient offers from lenders to satisfy the loan then the system should inform the borrower that it is not possible to provide a quote at that time.

Assumptions:
- The Rate column in the .csv file is annual rate.
- The Available column in the .csv file is the max amount that each lender can give. 


# Pre-requisites to run the loanCalculator
- pip install pep8-naming
- pip install numpy


# Usage of the script

The application should take arguments in the form: 
cmd> [application] [market_file] [loan_amount] 
main.py market.csv 1500
 
The application should produce output in the form: 
cmd> [application] [market_file] [loan_amount] 
Requested amount: £XXXX 
Rate: X.X% 
Monthly repayment: £XXXX.XX 
Total repayment: £XXXX.XX

# Run the unittests
python -m unittest discover -v

# Improvements
- Float arithmetics can be substituted with Decimal.
I had issues with np.rate calculations so I used float. 

- The formulas for the calculations are based on:
https://www.vertex42.com/ExcelArticles/amortization-calculation.html
Other formulas may give different results. 


 
