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
    monthlyPayment = 10
    unpaidBalance = balance

    while unpaidBalance > 0:
        for i in range(12):
            unpaidBalance = (unpaidBalance - monthlyPayment) + (unpaidBalance - monthlyPayment)*annualInterestRate/12
        if unpaidBalance > 0:
            monthlyPayment += 10
            unpaidBalance = balance
    return monthlyPayment

starttime = time.time()
print("Lowest Payment: "+str(round(payment(100000000,0.2),2)))
endtime = time.time()
print(endtime-starttime)
