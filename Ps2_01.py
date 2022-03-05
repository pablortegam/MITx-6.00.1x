balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
for i in range(1,13):
    minpay=monthlyPaymentRate*balance
    unpaidbal=balance-minpay
    interest=round(((annualInterestRate/12)*unpaidbal),2)
    balance=round(+unpaidbal+interest,2)
    i=-1
print('Remaining balance: '+str(balance))
