import numpy as np

# Creation
a = np.array([10, 20, 30, 40, 50, 60])
print("Original Array:", a)

# Indexing
print("Indexing:", a[2])

# Slicing
print("Slicing:", a[1:5])

# Reshaping
b = np.array([1, 2, 3, 4, 5, 6])
print("Reshaped Array:")
print(b.reshape(2, 3))

# Mathematical Operations
print("Addition:", a + 5)
print("Subtraction:", a - 5)
print("Multiplication:", a * 2)
print("Division:", a / 2)

print("Square:", np.square(a))
print("Square Root:", np.sqrt(a))
print("Sum:", np.sum(a))
print("Mean:", np.mean(a))