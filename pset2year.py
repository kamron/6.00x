balance = 4773
annualInterestRate = 0.2

remainingBalance = balance
monthlyPayment = 10
while remainingBalance > 0:
	remainingBalance = balance
	for month in range (1,13):
		remainingBalance-=monthlyPayment
		remainingBalance+=remainingBalance*(annualInterestRate/12)
	else:
		monthlyPayment += 10
print('Lowest Payment: ' + str(round(monthlyPayment-10, 2)))
