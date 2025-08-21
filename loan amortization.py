
principal = float(input('enter the sum of money to be returned: £'))
interest_rate = float(input('enter the interest rate on this loan: %'))
interest_rate = interest_rate/100
n = float(input('enter how long you have to pay this loan in months: '))
r = interest_rate/12

if interest_rate == 0:
    A = principal/n
else:
    A = principal * (r * (1 + r) ** n) / (-1 + (1 + r) ** n)


total_payment = A * n
total_interest = total_payment - principal

print(f'\nMonthly payment: £{A:.2f}')
print(f'Total repayment: £{total_payment:.2f}')
print(f'Total interest paid: £{total_interest:.2f}')
