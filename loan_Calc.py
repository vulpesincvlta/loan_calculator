import math

print('Enter the loan principal: ')

loan_principal = int(input())

print(f'What do you want to calculate? \ntype "m" - for number of monthly payments,\ntype "p" - for the monthly payment:')

a = input()

if a == 'm':

    print('Enter the monthly payment: ')
    payment = int(input())
    pay_time = loan_principal / payment
    t = math.ceil(pay_time)
    if t == 1:
        print(f'It will take {t} month to repay the loan')
    else:
        print(f'It will take {t} months to repay the loan')

elif a == 'p':
    print('Enter the number of months:')
    months = int(input())
    month_pay = loan_principal / months

    last = loan_principal - ((months - 1) * math.ceil(month_pay))

    if loan_principal % months == 0:
        print(f'Your monthly payment = {math.ceil(month_pay)}')
    else:
        print(f'Your monthly payment = {math.ceil(month_pay)} and the last payment = {last}.')


else:
    print('error')
