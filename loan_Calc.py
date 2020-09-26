import math



print(f'What do you want to calculate? \ntype "n" for number of monthly payments, \ntype "a" for annuity monthly payment amount,\ntype "p" for loan principal:')
a = input()

if a == 'n':

    print('Enter the loan principal:')
    loan_principal = int(input())

    print('Enter the monthly payment:')
    monthly_payment = int(input())

    print('Enter the loan interest:')
    li = float(input())

    ni = li / (12 * 100)
    fom = monthly_payment / (monthly_payment - ni * loan_principal)
    num_months = math.log(fom , ni + 1 )
    rounded = math.ceil(num_months)

    if rounded % 12 == 0:
        print(f'It will take {rounded // 12} years to repay this loan!')
    else:
        print(f'It will take {rounded // 12} years and {rounded % 12} months to repay this loan!')

elif a == 'a':
    print('Enter the loan principal:')
    lp = int(input())
    print('Enter the number of periods:')
    np = int(input())
    print('Enter the loan interest:')
    li = float(input())
    i = li / (12 * 100)
    p = (1+ i) **  np
    mp = lp * ((i * p)/(p - 1))
    print(f'Your monthly payment = {math.ceil(mp)}!')

elif a == 'p':

    print('Enter the annuity payment:')
    ap = float(input())
    print('Enter the number of periods:')
    np = int(input())
    print('Enter the loan interest:')
    li = float(input())

    i = li / (12 * 100)
    p = (1+ i) **  np

    lp = ap / ((i * p)/(p - 1))
    print(f'Your loan principal = {math.floor(lp)}!')


else:
    print('error')
