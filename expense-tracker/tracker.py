import json
import argparse
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='command')
add_parser = subparsers.add_parser('add')
add_parser.add_argument('--amount',type=float,required=True)
add_parser.add_argument('--category',type=str,required=True)
add_parser.add_argument('--date',type=str,required=True)
list_parser = subparsers.add_parser('list')
list_parser.add_argument('--category',type=str,required=False)
args = parser.parse_args()
if args.command =='add':
    new_expense = {'amount':args.amount,'category':args.category,'date':args.date}
    try:
        with open('expense.json','r') as f:
            expenses=json.load(f)
    except FileNotFoundError:
        expenses =[]

    expenses.append(new_expense)

    with open('expense.json','w') as f:
        json.dump(expenses,f)
elif args.command=='list':
    try:
        with open('expense.json', 'r') as f:
            expenses = json.load(f)
    except FileNotFoundError:
        expenses = []
    for expense in expenses:
        if args.category is None or expense['category']==args.category:
            print(f"${expense['amount']:.2f} - {expense['category']} - {expense['date']}")
        