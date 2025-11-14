**Personal Expense Tracker**

A simple command-line personal expense tracker written in Python.

**Project Files**:
- `Expence Tracker.py`: Main script — add expenses and view a simple summary.
- `expenses.csv`: Data file where each expense is stored as `amount,category,date`.
- `README.md`: This file (project overview and usage).

**Description**:
- **Purpose**: Quickly log expenses and view the total spent.
- **How it works**: The script appends each expense to `expenses.csv`. A summary option reads the file and prints the total amount.

**Features**:
- Add an expense with amount and category (date is auto-set to the current date).
- View the total of all recorded expenses.
- Stores expenses in a simple CSV file that can be opened in a spreadsheet program.

**Requirements**:
- Python 3.6 or newer (uses `datetime` and `csv` from the standard library).

**Usage**:
1. Open a terminal and change into the project folder:

```
cd "c:\Users\bhema\OneDrive\Desktop\My Projects\Python projects\Personal Expense Tracker"
```

2. Run the script with Python:

```
python "Expence Tracker.py"
```

3. Follow the on-screen menu:
- Choose `1` to add an expense. Enter the amount and category when prompted.
- Choose `2` to view the total expenses.
- Choose `3` or any other key to exit.

**CSV Format**:
- Each line in `expenses.csv` follows the format: `amount,category,YYYY-MM-DD`.
- Example line: `100.0,groceries,2025-11-15`.

**Notes & Suggestions**:
- The script creates `expenses.csv` the first time it runs if it doesn't exist.
- Amounts are stored as plain floats; consider formatting or validation if you need stronger guarantees (currency handling, rounding).
- Possible improvements:
  - Add date input so the user can record historic expenses.
  - Add per-category summaries and monthly breakdowns.
  - Add input validation and error handling (non-numeric amounts, empty categories).
  - Add a simple UI or export features (JSON, Excel).

**License**:
- This repository contains simple example code — use and modify it as you like.

**Contact / Questions**:
- If you want help extending the tracker (reports, category totals, GUI), tell me what you'd like to add and I can implement it.
