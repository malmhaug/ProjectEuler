"""
Problem: In the number 600851475143, what is the largest prime factor.

Example: Prime factors in the number 13195 is [5,7,13,29].

Prime factor: Positive natural number which a prime number can be divided by, and result in a integer.
"""

import time

start_time = time.time()
target = 600851475143
result = 0
test_value = 1
multiplied_prime_factors = 1


while True:
    if target % test_value == 0:
        multiplied_prime_factors *= test_value

    if multiplied_prime_factors == target:
        result = test_value
        break
    else:
        test_value += 1

print(test_value, time.time() - start_time)

