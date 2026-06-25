\# Personal Expense Tracker



A Python application to record, manage, and summarize personal expenses using CSV file handling.



\## Features



\* Add expense records with date, description, category, and amount

\* Store expense data in a CSV file

\* Display all recorded expenses in a formatted table

\* Generate a category-wise spending summary

\* Find the highest expense recorded



\## Technologies Used



\* Python

\* CSV Module

\* File Handling

\* `datetime`

\* `os`



\## Concepts Demonstrated



\* Functions

\* File handling

\* Dictionaries

\* Lists

\* Loops

\* Data processing

\* CSV file operations



\## How to Run



\### 1. Clone the repository



```bash

git clone https://github.com/prajwalnaik98/Personal-Expense-Tracker.git

cd Personal-Expense-Tracker

```



\### 2. Run the program



```bash

python expense\_tracker.py

```



The program automatically creates an `expenses.csv` file if it does not already exist.



\## Project Structure



```text

Personal-Expense-Tracker/

│

├── expense\_tracker.py

├── README.md

└── .gitignore

```



> \*\*Note:\*\* `expenses.csv` is generated automatically when the program runs.



\## Sample Output



```text

Added: Groceries | Food | Rs.850.00

Added: Bus pass | Travel | Rs.500.00



All Expenses

\-------------------------------------------------------

Date         Description        Category     Amount

\-------------------------------------------------------

25-06-2026   Groceries          Food       Rs.850.00

25-06-2026   Bus pass           Travel     Rs.500.00

...



Summary by Category

\------------------------------

Food            Rs.1090.00

Travel          Rs. 590.00

Bills           Rs.1899.00

Study           Rs. 120.00

\------------------------------

Total           Rs.3699.00



Highest expense: Electricity bill — Rs.1200.00

```



\## Customization



To add your own expenses, edit the `main()` function in `expense\_tracker.py`:



```python

add\_expense("Your item", "Category", amount)

```



You can use categories such as:



\* Food

\* Travel

\* Bills

\* Study

\* Other



Or create your own categories.



\## Future Improvements



\* Menu-driven interface

\* Search expenses by category

\* Filter expenses by date

\* Monthly expense reports

\* Charts and visualizations using Matplotlib



\## Author



\*\*Prajwal Naik\*\*



