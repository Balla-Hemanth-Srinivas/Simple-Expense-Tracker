import csv
from datetime import datetime

class Expense:
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date

class ExpenseTracker:
    FILE = "expenses.csv"

    def __init__(self):
        try:
            open(self.FILE, "x").close()
        except FileExistsError:
            pass

    def add_expense(self, expense):
        with open(self.FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([expense.amount, expense.category, expense.date])

    def show_summary(self):
        total = 0
        with open(self.FILE) as f:
            reader = csv.reader(f)
            for row in reader:
                total += float(row[0])
        print(f"Total Expenses: ₹{total}")

tracker = ExpenseTracker()

while True:
    print("\n1. Add Expense\n2. Summary\n3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        amount = float(input("Amount: "))
        category = input("Category: ")
        date = datetime.now().strftime("%Y-%m-%d")
        tracker.add_expense(Expense(amount, category, date))
        print("Expense saved.")

    elif choice == "2":
        tracker.show_summary()

    else:
        break
