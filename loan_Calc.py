import argparse
import math
import sys


parser = argparse.ArgumentParser()
parser.add_argument("--type", help="choose between loan calculation")
parser.add_argument("--payment", help="monthly payment amount")
parser.add_argument("--principal", help="loan principal value")
parser.add_argument("--periods", help=" denotes the number of months needed to repay the loan")
parser.add_argument("--interest", help="loan interest")

args = parser.parse_args()

if len(sys.argv) < 4:
    print('Incorrect parameters')
else:
    if args.interest is None:
        print('Incorrect parameters')
    elif args.interest is not None:
        if args.type == 'diff':
            lp = int(args.principal)
            li = float(args.interest)
            payments = int(args.periods)
            i = li / (12 * 100)
            op = 0
            for m in range(payments):
                diffp = (lp / payments) +  (i * (lp - ((lp * ((m + 1) - 1))/(payments))))
                print(f'Month {m + 1}: payment is {math.ceil(diffp)}')
                op += math.ceil(diffp)
            print(f'Overpayment: {math.ceil(op) - lp}')
        elif args.type == 'annuity':
            if args.principal is not None:
                if args.payment is not None:
                    lp = int(args.principal)
                    ap = int(args.payment)
                    li = float(args.interest)
                    i = li / (12 * 100)
                    fom = ap / (ap - i * lp)
                    num_months = math.log(fom , i + 1 )
                    rounded = math.ceil(num_months)
                    op = (rounded * ap) - lp
                    if rounded % 12 == 0:
                        print(f'It will take {rounded // 12} years to repay this loan! \nOverpayment: {math.ceil(op)}')
                    else:
                        print(f'It will take {rounded // 12} years and {rounded % 12} months to repay this loan! \nOverpayment: {math.ceil(op)}')
                elif args.payment is None:
                    lp = int(args.principal)
                    np = int(args.periods)
                    li = float(args.interest)
                    i = li / (12 * 100)
                    p = (1 + i) **  np
                    mp = lp * ((i * p)/(p - 1))
                    op = math.ceil(mp) * np - lp
                    print(f'Your annuity payment = {math.ceil(mp)}!')
                    print(f'Overpayment: {math.ceil(op)}')
            if args.principal is None:
                ap = int(args.payment)
                li = float(args.interest)
                np = int(args.periods)
                i = li / (12 * 100)
                p = (1 + i) **  np
                lp = ap / ((i * p)/(p - 1))
                print(f'Your loan principal = {math.floor(lp)}!')
                op = (ap * np) - lp
                print(f'Overpayment: {math.ceil(op)}')
        else:
            print('Incorrect parameters')
