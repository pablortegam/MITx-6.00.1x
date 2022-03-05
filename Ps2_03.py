balance = 999999
annualInterestRate = 0.18
llim=balance/12
hlim=(balance*((1+(annualInterestRate/12))**12))/12
ibalance=balance
monthlyPayment=round((llim+hlim)/2,2)
while hlim-llim>0.01:
        for i in range(0,12):
            unpaidbal=balance-monthlyPayment
            interest=round(((annualInterestRate/12)*unpaidbal),2)
            balance=round(+unpaidbal+interest,2)
        if balance >0.01:
            llim=monthlyPayment
            monthlyPayment=round((llim+hlim)/2,2)
            balance=ibalance
        if balance <0.01:
            hlim=monthlyPayment
            monthlyPayment=round((llim+hlim)/2,2)
            balance=ibalance
else:
    print('Lowest Payment: '+str(round(monthlyPayment,2)))
