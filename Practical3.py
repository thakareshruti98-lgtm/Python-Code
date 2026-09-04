# Program to perform various operations on a Python list

# Creating a list
numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

# Accessing elements
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])

# Adding elements
numbers.append(60)
print("After append():", numbers)

numbers.insert(2, 25)
print("After insert():", numbers)

# Removing elements
numbers.remove(25)
print("After remove():", numbers)

removed = numbers.pop()
print("Popped Element:", removed)
print("After pop():", numbers)

# Finding elements
print("Index of 30:", numbers.index(30))
print("Count of 20:", numbers.count(20))

# Sorting
numbers.sort()
print("After sort():", numbers)

# Reversing
numbers.reverse()
print("After reverse():", numbers)

# Length of list
print("Length of List:", len(numbers))

# Maximum and minimum
print("Maximum Element:", max(numbers))
print("Minimum Element:", min(numbers))

# Sum of elements
print("Sum of Elements:", sum(numbers))

# Slicing
print("Sliced List:", numbers[1:4])

# Checking membership
print("Is 30 present?", 30 in numbers)