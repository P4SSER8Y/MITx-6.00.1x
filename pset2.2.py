""" Problem Set 2: Problem 2 - PAYING DEBT OFF IN A YEAR """

# Predefined
balance = 3926
annualInterestRate = 0.2

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
    
payment = 10
while calculateBalance(balance, annualInterestRate, payment) > 0:
    payment += 10
print "Lowest Payment:", payment