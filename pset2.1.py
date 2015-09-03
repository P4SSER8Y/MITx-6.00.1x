""" Problem Set 2 Problem 1: Paying the Minumum """

# ======= Predefine =======

balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# ======== Source Code =========

monthlyInterestRate = annualInterestRate / 12.0
totalPayment = 0

for _ in range(1,13):
    print "Month:", _
    payment = balance * monthlyPaymentRate
    totalPayment += payment
    balance -= payment
    balance += balance * monthlyInterestRate
    print "Minimum monthly payment:", round(payment, 2)
    print "Remaining balance:", round(balance, 2)
    
print "Total paid:", round(totalPayment, 2)
print "Remaining balance:", round(balance, 2)