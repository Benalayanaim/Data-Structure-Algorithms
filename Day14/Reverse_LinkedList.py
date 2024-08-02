#Description of the problem
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/30734980#overview
#https://leetcode.com/problems/reverse-linked-list/description/




#Solution N1:

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create the linked list 1 -> 2 -> 3 -> 4
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

def reverseLinkedList(head):
    prev = None
    current = head
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

# Helper function to print the linked list
def print_linkedlist(node):
    while node:
        print(node.value, end=" -> " if node.next else "")
        node = node.next
    print()

# Print original linked list
print("Original linked list:")
print_linkedlist(head)

# Reverse the linked list
reversed_head = reverseLinkedList(head)

# Print reversed linked list
print("Reversed linked list:")
print_linkedlist(reversed_head)



#Explanation in the folder reservesol1





# Helper function to convert a linked list to a list
"""def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.value)
        node = node.next
    return result

"""




#Another Solutions find in this link
"https://www.geeksforgeeks.org/reverse-a-linked-list/" 