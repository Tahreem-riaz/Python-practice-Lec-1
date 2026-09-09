"""
========================================================
       LECTURE 1 - FILE 4: TYPE CONVERSION
========================================================
Topics: Type Conversion, Type Casting, Implicit and
        Explicit Conversion
========================================================
"""

# ========================================================
# PART A: BASIC TYPE CASTING
# ========================================================

# Q1. Convert the following values:
#
#     45       → float
#     78.9     → int
#     250      → string
#
#     Print each converted value.


number1 = 45
number2 = 78.9
number3 = 250

converted_float = float(number1)
converted_int = int(number2)
converted_string = str(number3)

print("Float:", converted_float)
print("Integer:", converted_int)
print("String:", converted_string)

# --------------------------------------------------------

# Q2. A product price is stored as the string:
#
#     "1299.50"
#
#     Convert it into a float and calculate the price
#     after adding 100 PKR.

product_price = "1299.50"

product_price = float(product_price)
new_price = product_price + 100

print("New Price:", new_price, "PKR")

# --------------------------------------------------------

