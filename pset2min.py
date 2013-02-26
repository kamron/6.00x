balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
balance=balance-monthlyPaymentRate

totalPaid=0
unpaidBalance=balance
for month in range (1,13):
	minPayment=unpaidBalance*monthlyPaymentRate
	totalPaid+=minPayment
	unpaidBalance=unpaidBalance-minPayment
	print('Month: ' + str(month))
	print('Minimum monthly payment: ' + str(round(minPayment, 2)))
	unpaidBalance+=unpaidBalance*(annualInterestRate/12)
	print('Remaining balance: ' + str(round(unpaidBalance, 2)))
print('Total paid: ' + str(round(totalPaid, 2)))
print('Remaining balance: ' + str(round(unpaidBalance, 2)))
