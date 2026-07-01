# Personal Expense Tracker

A beginner-friendly Python project that helps users record daily expenses, store them in a CSV file, and generate simple spending summaries.

---

## Project Description

This project is a console-based expense tracker built using Python. It allows users to record expenses with details such as date, description, category, and amount. All records are saved in a CSV file, making the data available even after the program is closed. The application also provides category-wise spending summaries and identifies the highest expense.

---

## Features

- Add new expense records
- Store expense data in a CSV file
- Display all expenses in a formatted table
- Generate category-wise spending summaries
- Calculate total expenses
- Identify the highest expense
- Automatically creates the data file if it doesn't exist

---

## Concepts Used

| Concept | Implementation |
|---|---|
| Functions with docstrings | Organizing reusable code |
| CSV file handling | Reading and writing expense records |
| Dictionaries | Storing category-wise totals |
| Loops | Processing expense records |
| `datetime` module | Recording the current date |
| `os` module | Checking whether the CSV file exists |
| f-strings | Formatting console output |
| Conditionals | Handling empty files and calculations |

---

## How to Run

### Step 1 — Install Python

Ensure Python 3.8 or later is installed.

```bash
python --version
```

### Step 2 — Clone the repository

```bash
git clone https://github.com/prajwalnaik98/Personal-Expense-Tracker.git
cd Personal-Expense-Tracker
```

### Step 3 — Execute the program

```bash
python expense_tracker.py
```

### Step 4 — View the results

The program will:

- Add expense records
- Save data to `expenses.csv`
- Display all recorded expenses
- Show category-wise spending
- Display the highest expense

---

## Project Structure

```text
Personal-Expense-Tracker/
│
├── expense_tracker.py
├── expenses.csv
├── README.md
└── .gitignore
```

---

## Functions Overview

| Function | Purpose |
|---|---|
| `create_file()` | Creates the CSV file if it doesn't exist |
| `add_expense()` | Adds a new expense record |
| `read_expenses()` | Reads all saved expenses |
| `display_expenses()` | Displays expenses in a formatted table |
| `category_summary()` | Calculates spending by category |
| `highest_expense()` | Finds the most expensive transaction |
| `main()` | Runs the complete application |

---

## Sample Output

```text
Added: Groceries | Food | Rs.850.00
Added: Bus Pass | Travel | Rs.500.00
Added: Electricity Bill | Bills | Rs.1200.00
...

All Expenses
-------------------------------------------------------
Date         Description          Category      Amount
-------------------------------------------------------
25-06-2026   Groceries            Food       Rs.850.00
25-06-2026   Bus Pass             Travel     Rs.500.00
25-06-2026   Electricity Bill     Bills      Rs.1200.00
...

Summary by Category
--------------------------------
Food          Rs.1090.00
Travel        Rs.590.00
Bills         Rs.1899.00
Study         Rs.120.00
--------------------------------
Total          Rs.3699.00

Highest Expense: Electricity Bill — Rs.1200.00
```

---

## Customization

To add your own expenses, edit the `main()` function inside `expense_tracker.py`:

```python
add_expense("Description", "Category", amount)
```

You can use the default categories:

- Food
- Travel
- Bills
- Study
- Other

Or create your own categories based on your requirements.

---

## Author

**Developed by:** **Prajwal Naik**

This project was created to strengthen practical Python programming skills, including file handling, CSV operations, dictionaries, loops, functions, and working with Python's standard library.
