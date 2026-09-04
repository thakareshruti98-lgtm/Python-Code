# Student Data System

# Taking input from the user
name = input("Enter student name: ")
roll_no = int(input("Enter roll number: "))
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))
course = input("Enter course: ")
is_passed = marks >= 40

# Displaying student information
print("\n----- Student Details -----")
print("Name:", name)
print("Roll Number:", roll_no)
print("Age:", age)
print("Marks:", marks)
print("Course:", course)
print("Passed:", is_passed)

# Checking result using conditional statement
if is_passed:
    print("Result: PASS")
else:
    print("Result: FAIL")