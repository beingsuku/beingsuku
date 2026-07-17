from datetime import date
expenses=[]
import csv

def save_expenses():
    with open("expenses.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["amount", "category", "date"])
        writer.writeheader()
        writer.writerows(expenses)

def load_expenses():
    global expenses
    try:
        with open("expenses.csv", "r") as f:
            reader = csv.DictReader(f)
            expenses = list(reader)
    except FileNotFoundError:
        expenses = []

def total_spending():
        total=sum(float(x['amount']) for x in expenses)
        print(total)

def category_breakdown():
    breakdown = {}
    for x in expenses:
        category = x["category"]
        amount = float(x["amount"])
        if category not in breakdown:
            breakdown[category] = 0
        breakdown[category] += amount
    
    for category, total in breakdown.items():
        print(f"{category}: {total}")
def add_expense():
    try :
        amount=float(input("Enter the amount:"))
    except ValueError:
        print("Enter valid Number")
        return
    category=input("Enter category:")
    today = date.today()

    entry = {"amount":amount,"category":category,"date":today}

    expenses.append(entry)
    print("Expense added!")
    save_expenses()

def view_expense():
    if not expenses:
        print("You haven't spent yet")
        return 
    for x in expenses:
         print(f"Amount: {x['amount']} | Category: {x['category']} | Date: {x['date']}")

def main():
    load_expenses()
    while True:
        print("1.Add expense 2.View expenses 3.View total spending 4.breakdown 5.Exit")
        try:
            choice=int(input("Enter your choice:"))
        except(ValueError,IndexError):
            print("Enter Valid one!")
            continue
        match choice :
            case 1:
                add_expense()
            case 2:
                view_expense()
            case 3:
                total_spending()
            case 4:
                category_breakdown()
            case 5:
                print("See you after new spending!")
                break
            case _ :
                print("Enter valid choice!")

main()

         
