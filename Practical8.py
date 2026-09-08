# Practical 8: Linked List - Singly, Doubly and Circular

# Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

print("Singly Linked List:")
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

n1.next = n2
n2.next = n3

temp = n1
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")


# Doubly Linked List
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

print("\nDoubly Linked List:")
d1 = DNode(10)
d2 = DNode(20)
d3 = DNode(30)

d1.next = d2
d2.prev = d1
d2.next = d3
d3.prev = d2

temp = d1
while temp:
    print(temp.data, end=" <-> ")
    temp = temp.next
print("None")


# Circular Linked List
print("\nCircular Linked List:")
c1 = Node(10)
c2 = Node(20)
c3 = Node(30)

c1.next = c2
c2.next = c3
c3.next = c1

temp = c1
for i in range(3):
    print(temp.data, end=" -> ")
    temp = temp.next
print("(Back to 10)")