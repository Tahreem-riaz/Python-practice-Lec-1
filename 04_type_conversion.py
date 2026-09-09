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

# Q3. A player's score is stored as:
#
#     score = "875"
#
#     Convert it into an integer and add 125 points.
#
#     Print the new score.

score = "875"

score = int(score)
new_score = score + 125

print("New Score:", new_score)


# ========================================================
# PART B: STRING CONVERSION
# ========================================================

# Q4. Create an integer containing a year.
#
#     Convert the year into a string and combine it
#     with another string to create a sentence.
#
#     Example idea:
#     "The current year is ..."




