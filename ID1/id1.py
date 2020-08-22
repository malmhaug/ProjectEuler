"""
Problem: Using only natural numbers, find the sum of all the multiplies of 3 or 5 below 1000.

Example: Using 10 as a limit, all multiplies of 3 or 5 below this limit is [3,5,9]. The sum of these multiplies is 23.

Natural number: Positive integers, like 0,1,2,3,4,etc....
"""

import time

start_time = time.time()
result = 0

for x in range(1000):
    if (x % 3 == 0) or (x % 5 == 0):
        result += x

print(result, time.time() - start_time)
