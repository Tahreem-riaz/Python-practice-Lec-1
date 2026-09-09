"""
========================================================
          LECTURE 1 - FILE 5: MINI PROJECT
========================================================
Project: Personal Budget Calculator

Concepts Used:
- Variables
- Data Types
- Arithmetic Operators
- Comparison Operators
- Logical Operators
- Type Conversion
- User Input
========================================================
"""

# ========================================================
# PERSONAL BUDGET CALCULATOR
# ========================================================

print("=" * 50)
print("          PERSONAL BUDGET CALCULATOR")
print("=" * 50)

# --------------------------------------------------------
# STEP 1: GET USER INFORMATION
# --------------------------------------------------------

# Ask the user for:
# - Name
# - Monthly budget
# - Food expenses
# - Transport expenses
# - Entertainment expenses


# Write your code below:

name = input("Enter your name: ")
monthly_budget = float(input("Enter your monthly budget: "))
food_expenses = float(input("Enter your food expenses: "))
transport_expenses = float(input("Enter your transport expenses: "))
entertainment_expenses = float(input("Enter your entertainment expenses: "))


# --------------------------------------------------------
# STEP 2: CALCULATE TOTAL EXPENSES
# --------------------------------------------------------

# Calculate the total amount spent.


# Write your code below:

total_expenses = food_expenses + transport_expenses + entertainment_expenses

print("Total Expenses:", total_expenses, "PKR")

# --------------------------------------------------------
# STEP 3: CALCULATE REMAINING MONEY
# --------------------------------------------------------

# Calculate how much money remains after expenses.


# Write your code below:

remaining_money = monthly_budget - total_expenses

print("Remaining Money:", remaining_money, "PKR")


