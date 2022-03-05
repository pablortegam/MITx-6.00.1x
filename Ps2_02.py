balance = 320000
annualInterestRate = 0.2
monthlyPayment = 0.01
ibalance=balance
while balance>0:
    for i in range(0,12):
        unpaidbal=balance-monthlyPayment
        interest=round(((annualInterestRate/12)*unpaidbal),2)
        balance=round(+unpaidbal+interest,2)
    if balance >0:
        monthlyPayment+=0.01
        balance=ibalance
else:
    print('Lowest Payment: '+str(round(monthlyPayment)))
