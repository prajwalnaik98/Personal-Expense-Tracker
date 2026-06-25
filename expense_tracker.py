#Personal Expense Tracker



import csv
import os
from datetime import date


FILENAME = "expenses.csv"


# ── Step 1: Create the CSV file with headers if it does not exist yet ─────────
def setup_file():
    """Create the expenses CSV file with column headers if it does not exist."""
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Description", "Category", "Amount"])
        print(f"Created new file: {FILENAME}")


# ── Step 2: Add a new expense ─────────────────────────────────────────────────
def add_expense(description, category, amount):
    """
    Add a new expense record to the CSV file.

    Parameters:
        description (str): What the expense was for.
        category    (str): Category such as Food, Travel, Bills, Other.
        amount      (float): How much was spent.
    """
    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    today = date.today().strftime("%d-%m-%Y")

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([today, description, category, amount])

    print(f"Added: {description} | {category} | Rs.{amount:.2f}")


# ── Step 3: Read all expenses from the file ───────────────────────────────────
def load_expenses():
    """
    Read all expense records from the CSV file.

    Returns:
        list: A list of dictionaries, one per expense row.
    """
    expenses = []

    with open(FILENAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["Amount"] = float(row["Amount"])
            expenses.append(row)

    return expenses


# ── Step 4: Display all expenses ──────────────────────────────────────────────
def show_all_expenses(expenses):
    """Print all expenses in a formatted table."""
    if not expenses:
        print("No expenses recorded yet.")
        return

    print()
    print("-" * 55)
    print(f"{'Date':<12} {'Description':<18} {'Category':<10} {'Amount':>8}")
    print("-" * 55)

    for expense in expenses:
        print(
            f"{expense['Date']:<12} "
            f"{expense['Description']:<18} "
            f"{expense['Category']:<10} "
            f"Rs.{expense['Amount']:>6.2f}"
        )

    print("-" * 55)


# ── Step 5: Show a summary by category ────────────────────────────────────────
def show_summary(expenses):
    """Print total spending per category and the grand total."""
    if not expenses:
        print("No expenses to summarise.")
        return

    # Build a dictionary of category totals
    category_totals = {}
    for expense in expenses:
        category = expense["Category"]
        amount   = expense["Amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    grand_total = sum(category_totals.values())

    print()
    print("Summary by Category")
    print("-" * 30)
    for category, total in category_totals.items():
        print(f"  {category:<15} Rs.{total:>7.2f}")
    print("-" * 30)
    print(f"  {'Total':<15} Rs.{grand_total:>7.2f}")
    print()


# ── Step 6: Show the most expensive item ──────────────────────────────────────
def show_highest_expense(expenses):
    """Print the single most expensive item recorded."""
    if not expenses:
        return

    highest = expenses[0]
    for expense in expenses:
        if expense["Amount"] > highest["Amount"]:
            highest = expense

    print(f"Highest expense: {highest['Description']} — Rs.{highest['Amount']:.2f}")


# ── Main program ──────────────────────────────────────────────────────────────
def main():
    setup_file()

    # Adding sample expenses — students can change these to their own
    add_expense("Groceries",      "Food",    850.00)
    add_expense("Bus pass",       "Travel",  500.00)
    add_expense("Electricity bill","Bills",  1200.00)
    add_expense("Lunch",          "Food",    180.00)
    add_expense("Notebook",       "Study",   120.00)
    add_expense("Auto ride",      "Travel",   90.00)
    add_expense("Internet bill",  "Bills",   699.00)
    add_expense("Coffee",         "Food",     60.00)

    # Load everything back from the file
    expenses = load_expenses()

    # Display results
    print("\nAll Expenses")
    show_all_expenses(expenses)
    show_summary(expenses)
    show_highest_expense(expenses)


if __name__ == "__main__":
    main()