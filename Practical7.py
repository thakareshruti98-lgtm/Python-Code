# Practical 7: Linear Search and Binary Search

arr = [10, 20, 30, 40, 50, 60]

print("Array:", arr)

# Linear Search
key = int(input("Enter element to search using Linear Search: "))

found = False
for i in range(len(arr)):
    if arr[i] == key:
        print("Linear Search: Element found at index", i)
        found = True
        break

if not found:
    print("Linear Search: Element not found")

# Binary Search
key = int(input("Enter element to search using Binary Search: "))

low = 0
high = len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        print("Binary Search: Element found at index", mid)
        found = True
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Binary Search: Element not found")