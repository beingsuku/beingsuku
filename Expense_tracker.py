expense=[]

from datetime import date
import csv

def save_expenses():
    with open("expenses.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["amount", "category", "date"])
        writer.writeheader()
        writer.writerows(expense)

def load_expenses():
    global expense
    try:
        with open("expenses.csv", "r") as f:
            reader = csv.DictReader(f)
            expense = list(reader)
    except FileNotFoundError:
        expense = []

def add_expense():
    try:
        amount=float(input("Enter the amount:"))
    except ValueError:
        print("Enter a valid number!")
        return
    category = input("Enter the category:")
    today = date.today()

    entry = {f"Amount":amount,"category":category,"date":today}
    expense.append(entry)

def view_expenses():
    if not expense :
        print("This is empty,u have not spent yet!")
    for x in expense :
        print( x )

def total_spending():
    for x in expense:
        total=sum(item["amount"] for item in expense)
        print(total)

def category_breakdown():
     pass

def main():
    load_expenses()
    while True:
        print("1.Add_expense 2.View_expense 3.Total_spending 4.Breakdown 5.Exit")
        try:
            choice = int(input("Enter a choice!"))
        except ValueError:
            print("Enter valid option!")
            continue
        match choice :
            case 1:
                add_expense()
                save_expenses()
            case 2:
                view_expenses()
            case 3:
                total_spending()
            case 4:
                category_breakdown()
            case 5:
                print("Saved changes!")
                break
            case _:
                print("Enter a valid choice")

main()