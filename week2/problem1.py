def remainigBalance(balance, annualInterestRate, monthlyPaymentRate):
    """
    For each month, calculates statements on the monthly payment and remaining balance.
    At the end of 12 months, prints out the remaining balance
    :param balance:             the outstanding balance on the credit card
    :param annualInterestRate:  annual interest rate as a decimal
    :param monthlyPaymentRate:  minimum monthly payment rate as a decimal
    :return: the remaining balance at the end of the year in the format: Remaining balance: 4784.0
    """
    monthlyPayment = 0

    for i in range(12):
        monthlyPayment = balance * monthlyPaymentRate
        balance = (balance - monthlyPayment) + (balance - monthlyPayment)*annualInterestRate/12

    return print("Remaining balance: " + str(round(balance,2)))

remainigBalance(484,0.2,0.04)