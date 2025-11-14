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
            with open(self.FILE, "x", encoding="utf-8") as f:
                f.write("Category, Cost, Time & Date\n")
        except FileExistsError:
            pass

    def add_expense(self, expense):
        formatted_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"{expense.category}, ₹{expense.amount}, {formatted_date}\n"

        with open(self.FILE, "a", encoding="utf-8") as f:
            f.write(line)

    def show_summary(self):
        total = 0
        with open(self.FILE, encoding="utf-8") as f:
            next(f)  # skip header
            for row in f:
                parts = row.strip().split(", ")
                cost = parts[1].replace("₹", "")
                total += float(cost)
        print(f"\nTotal Expenses: ₹{total}")


def get_valid_amount():
    while True:
        amount = input("Amount: ")
        try:
            return float(amount)
        except ValueError:
            print("❌ Invalid amount! Enter a numeric value.")


def get_valid_category():
    while True:
        category = input("Category: ").strip()
        if category.replace(" ", ""):  
            return category
        print("❌ Invalid category! Enter alphabetic characters only.")


def get_valid_menu_choice():
    while True:
        print("\n1. Add Expense\n2. Summary\n3. Exit")
        choice = input("Choose: ").strip()

        if choice in ["1", "2", "3"]:
            return choice

        print("❌ Invalid choice! Please enter 1, 2, or 3.")


# MAIN PROGRAM
tracker = ExpenseTracker()

while True:
    choice = get_valid_menu_choice()

    if choice == "1":
        amount = get_valid_amount()
        category = get_valid_category()
        date = datetime.now().strftime("%Y-%m-%d")
        tracker.add_expense(Expense(amount, category, date))
        print("✔ Expense saved successfully.")

    elif choice == "2":
        tracker.show_summary()

    else:
        print("👋 Exiting... Have a great day!")
        break
