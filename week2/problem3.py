import time
def payment(balance, annualInterestRate):
    """
    Program that calculates the minimum fixed monthly payment
            needed in order pay off a credit card balance within 12 months.
    :param balance:             the outstanding balance on the credit card
    :param annualInterestRate:  annual interest rate as a decimal
    :return: The program should print out one line: the lowest monthly payment
             that will pay off all debt in under 1 year
    """
    lowerbound = balance/12
    upperbound = balance*((1+annualInterestRate/12)**12)/12
    monthlyPayment = (lowerbound+upperbound)/2

    unpaidBalance = balance

    while round(abs(unpaidBalance),2) != 0.0:
        unpaidBalance = balance
        for i in range(12):
            unpaidBalance = (unpaidBalance - monthlyPayment) + (unpaidBalance - monthlyPayment)*annualInterestRate/12

        if round(unpaidBalance,2) > 0:
            lowerbound = monthlyPayment
            monthlyPayment = (lowerbound+upperbound)/2

        if round(unpaidBalance,2) < 0:
            upperbound = monthlyPayment
            monthlyPayment = (lowerbound + upperbound) / 2

    return print("Lowest Payment: "+str(monthlyPayment,2))


starttime = time.time()
print("Lowest Payment: "+str(round(payment(100000000,0.2),2)))
endtime = time.time()
print(endtime-starttime)
