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
summary_parser =subparsers.add_parser('summary')
delete_parser = subparsers.add_parser('delete')
delete_parser.add_argument('--index',type=int,required=True)
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
elif args.command =='summary':
    try:
        with open('expense.json','r') as f:
            expenses = json.load(f)
    except FileNotFoundError:
        expenses = []
    monthly_totals ={}
    for expense in expenses:
        parts = expense['date'].split('-')
        month_year = parts[0] + '-' + parts[2]
        if month_year in monthly_totals:
            monthly_totals[month_year] = monthly_totals[month_year] + expense['amount']
        else:
            monthly_totals[month_year] = expense['amount']

    for month_year,total in monthly_totals.items():
        print(f"{month_year}: ${total:.2f}")
elif args.command =='delete':
    try:
        with open('expense.json','r') as f:
            expenses =json.load(f)
    except FileNotFoundError:
        expenses = []
    if args.index <0 or args.index >= len(expenses):
                print("Invalid Index")
    else:
        removed = expenses.pop(args.index)
        with open('expense.json','w') as f:
            json.dump(expenses,f)
        print(f"Deleted: ${removed['amount']:.2f} - {removed['category']} - {removed['date']}")
 


        