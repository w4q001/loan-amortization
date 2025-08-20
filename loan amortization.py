principal = int(input('enter the sum of money to be returned: £'))
interest_rate = int(input('enter the interest rate on this loan: %'))
interest_rate = interest_rate/100
n = int(input('enter how long you have to pay this loan in months: '))
r = interest_rate/12

A = principal * (r*(1+r)**n)/(-1 + (1+r)**n)
print(f'your monthly payment is £{A:.2f}')
