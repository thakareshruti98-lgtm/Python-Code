# Program to perform operations on Tuple, Set and Dictionary

# ---------------- TUPLE ----------------
print("----- TUPLE OPERATIONS -----")

t = (10, 20, 30, 40, 20)

print("Original Tuple:", t)
print("First Element:", t[0])
print("Last Element:", t[-1])
print("Length:", len(t))
print("Count of 20:", t.count(20))
print("Index of 30:", t.index(30))
print("Sliced Tuple:", t[1:4])

# ---------------- SET ----------------
print("\n----- SET OPERATIONS -----")

s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

print("Set 1:", s1)
print("Set 2:", s2)

print("Union:", s1.union(s2))
print("Intersection:", s1.intersection(s2))
print("Difference:", s1.difference(s2))

s1.add(70)
print("After add():", s1)

s1.remove(70)
print("After remove():", s1)

print("Is 20 present?", 20 in s1)

# ---------------- DICTIONARY ----------------
print("\n----- DICTIONARY OPERATIONS -----")

student = {
    "Name": "Rahul",
    "Roll_No": 101,
    "Course": "Data Science",
    "Marks": 85
}

print("Original Dictionary:", student)

# Accessing values
print("Student Name:", student["Name"])
print("Student Marks:", student["Marks"])

# Adding a new key-value pair
student["Age"] = 19
print("After adding Age:", student)

# Updating a value
student["Marks"] = 90
print("After updating Marks:", student)

# Removing an item
student.pop("Age")
print("After removing Age:", student)

# Built-in dictionary functions
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Number of items:", len(student))