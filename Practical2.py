# Program to demonstrate different operators in Python

a = 10
b = 3

# Arithmetic Operators
print("----- Arithmetic Operators -----")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# Relational Operators
print("\n----- Relational Operators -----")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Logical Operators
print("\n----- Logical Operators -----")
print("a > 5 and b < 5:", a > 5 and b < 5)
print("a > 5 or b > 5:", a > 5 or b > 5)
print("not(a > 5):", not(a > 5))

# Bitwise Operators
print("\n----- Bitwise Operators -----")
print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)
print("~a:", ~a)
print("a << 1:", a << 1)
print("a >> 1:", a >> 1)

# Assignment Operators
print("\n----- Assignment Operators -----")
x = 10
print("Initial x:", x)

x += 5
print("x += 5:", x)

x -= 3
print("x -= 3:", x)

x *= 2
print("x *= 2:", x)

x //= 4
print("x //= 4:", x)

x %= 3
print("x %= 3:", x)