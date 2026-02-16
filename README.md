# 📘 Personal Expense Tracker (CLI)

A simple and beginner-friendly command-line application to record daily expenses and compute a running total.  
All expenses are saved in a readable CSV file, making it easy to open in Excel or extend with additional features.

---

## 📂 Project Files
- **`Expence Tracker.py`** — Main Python script (keeps the original filename spelling).
- **`expenses.csv`** — Created automatically on first use; stores all expense records.

---

## 🚀 Features
- Add expenses with **amount**, **category**, and **timestamp**.
- Stores data in a clean CSV format:
  ```
  category, ₹amount, YYYY-MM-DD HH:MM:SS
  ```
- Displays the **total of all expenses**.
- Input validation:
  - Prevents invalid amount entries  
  - Validates category text  
  - Handles invalid menu selections

---

## 🛠 Requirements
- **Python 3.6 or newer**  
- Uses only standard Python libraries (`csv`, `datetime`)

---

## ▶️ How to Run (PowerShell)

1. Navigate to the project folder:
   ```powershell
   cd "Your/Project/Path"
   ```

2. Run the script:
   ```powershell
   python "Expence Tracker.py"
   ```

3. Choose an option from the menu:
   - `1` → Add an expense  
   - `2` → View total expenses  
   - `3` → Exit the program  

---

## 📝 Example Session

```
1. Add Expense
2. Summary
3. Exit
Choose: 1
Amount: 150
Category: transport
✔ Expense saved successfully.

Choose: 2
Total Expenses: ₹250.0
```

---

## 📄 CSV Format

Example `expenses.csv` entry:

```
groceries, ₹1500.0, 2025-11-15 01:00:00
```

---

## ⚠️ Notes & Limitations
- Automatically creates `expenses.csv` if it doesn’t exist.
- Amounts are stored as floats.
- Date/time is assigned automatically.
- Designed to be simple and fully dependency-free.

---

## ➕ Future Improvements
- Category-wise reports  
- Monthly summaries  
- Delete/update entries  
- Tkinter GUI  
- Export to JSON / Excel  

---

## 📄 License
This project is free to use, modify, and adapt.
