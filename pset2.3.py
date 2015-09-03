""" Problem Set 2 - Problem 3: USING BISECTION SEARCH TO MAKE THE PROGRAM FASTER """

# Predefined
balance = 999999
annualInterestRate = 0.18

# Source Code
def calculateBalance(balance, annualInterestRate, payment):
    """ This function calculates the left balance after a year
        balance: the initial balance, a number
        annualInterestRate: the annual interest rate, a percentage
        payment: the fixed payment each month, a number
        return: a number, may be negative or zero """
    monthlyInterestRate = annualInterestRate / 12.0 
    for _ in range(1, 13):
        balance -= payment
        balance += balance * monthlyInterestRate
    return round(balance, 2)
    
def findLowestPayment(lower, upper, balance, annualInterestRate):
    """ Using Bisection Search in Recursion form 
        return a float number
    """
    if round(lower, 2) == round(upper, 2):
        return round(lower, 2)
    else:
        mid = (lower + upper) / 2.0
        if calculateBalance(balance, annualInterestRate, mid) <= 0:
            return findLowestPayment(lower, mid, balance, annualInterestRate)
        else:
            return findLowestPayment(mid, upper, balance, annualInterestRate)

lowerBound = balance / 12.0
upperBound = (balance * (1 + annualInterestRate / 12.0) ** 12) / 12.0
print "Lowest Payment:", findLowestPayment(lowerBound, upperBound, balance,\
                                           annualInterestRate)