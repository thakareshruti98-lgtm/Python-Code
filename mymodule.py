# User-defined module

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def square(n):
    return n * n

# Program to use user-defined and built-in Python modules

import mymodule
import math
import statistics

# Using user-defined module
a = 10
b = 5

print("----- User Defined Module -----")
print("Addition:", mymodule.add(a, b))
print("Multiplication:", mymodule.multiply(a, b))
print("Square of a:", mymodule.square(a))

# Using math module
print("\n----- Math Module -----")
print("Square root of 25:", math.sqrt(25))
print("Power of 2^3:", math.pow(2, 3))
print("Factorial of 5:", math.factorial(5))
print("Value of pi:", math.pi)

# Using statistics module
numbers = [10, 20, 30, 40, 50]

print("\n----- Statistics Module -----")
print("Mean:", statistics.mean(numbers))
print("Median:", statistics.median(numbers))