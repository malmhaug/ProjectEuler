"""
Problem: Calculate the largest palindrome made from the product of three-digit numbers

Example: Largest palindrome from the product of two-digit numbers => 9009 = 91 x 99.

Palindrome: 1001, 2002 and 3003. Same number read both ways.
"""

import time

start_time = time.time()

result = ""
number_1 = 100
number_2 = 100
multiplied_number = 0
palindrome = 0
product_1 = 0
product_2 = 0

while number_2 < 1000:
    for number_1 in range(100, 999):  # Count from 100 to 999
        multiplied_number = number_1 * number_2
        if (multiplied_number == int(str(multiplied_number)[::-1])) and multiplied_number > palindrome:  # Largest palindrome - check
            palindrome = multiplied_number
            product_1 = number_1
            product_2 = number_2
    number_2 += 1  # Increment second digit


result = str(product_1) + " * " + str(product_2) + " = " + str(palindrome)
print(result, time.time() - start_time)

