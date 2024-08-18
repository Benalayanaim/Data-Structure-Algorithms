#Desrition of the problem
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/31223044#overview
#https://leetcode.com/problems/add-two-numbers/description/



#Solution N°1:
def addTwoNumbers(l1, l2):
    # Initialize an empty list to store the result
    result = []
    carry = 0
    
    # Use two pointers to iterate through both lists
    i, j = 0, 0
    
    while i < len(l1) or j < len(l2):
        # Get the values from l1 and l2, or 0 if one list is shorter
        val1 = l1[i] if i < len(l1) else 0
        val2 = l2[j] if j < len(l2) else 0
        total = val1 + val2 + carry
        
        # Compute new digit and carry
        carry = total // 10
        new_digit = total % 10
        
        # Append the new digit to the result list
        result.append(new_digit)
        
        # Move to the next elements in l1 and l2
        i += 1
        j += 1
    
    # If there's a remaining carry, append it to the result list
    if carry:
        result.append(carry)
    
    return result

# Test cases
l1 = [2, 4, 3]  # Represents the number 342
l2 = [5, 6, 4]  # Represents the number 465

result = addTwoNumbers(l1, l2)  # Should represent the number 807

# Print the result list
print("Result List:")
print(result)


#Explabnation in the folder Addsol1










print("=============================================")

#SolutionN°2:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    # Dummy node
    dummy = ListNode()
    current = dummy
    carry = 0
    
    # Loop through both lists
    while l1 or l2:
        # Sum the values, if present, otherwise add 0
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        
        # Compute new digit and carry
        carry = total // 10
        new_digit = total % 10
        
        # Add the new digit to the current node
        current.next = ListNode(new_digit)
        current = current.next
        
        # Move to the next nodes in l1 and l2
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    # If there's a remaining carry, add a new node with carry value
    if carry:
        current.next = ListNode(carry)
    
    # Return the next node of dummy, which is the head of the result list
    return dummy.next

# Helper function to create a linked list from a list of integers
def create_linked_list(numbers):
    dummy = ListNode()
    current = dummy
    for number in numbers:
        current.next = ListNode(number)
        current = current.next
    return dummy.next

# Helper function to print a linked list
def print_linked_list(node):
    numbers = []
    while node:
        numbers.append(node.val)
        node = node.next
    print(" -> ".join(map(str, numbers)))

# Test cases
l1 = create_linked_list([2, 4, 3])  # Represents the number 342
l2 = create_linked_list([5, 6, 4])  # Represents the number 465

result = addTwoNumbers(l1, l2)  # Should represent the number 807

# Print the result linked list
print("Result Linked List:")
print_linked_list(result)



 
"""Explanation:
create_linked_list Function: This helper function takes a list of integers and converts it into a linked list. 
Each integer becomes a node in the linked list.

print_linked_list Function: This function takes a linked list node as input and prints the values in the linked list in a readable 
format (e.g., 7 -> 0 -> 8).

Test Case: The test case creates two linked lists representing the numbers 342 and 465. After calling the addTwoNumbers function, 
the result is expected to represent 807, which will be printed as 7 -> 0 -> 8.
"""






print("=======================================================")








#solution N°3:
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
 
    def addAtTail(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
        return self
 
def add2Numbers(l1, l2):
    carryForward = 0
    results = LinkedList()
    while l1 or l2 or carryForward:
        l1Value = l1.value if l1 else 0
        l2Value = l2.value if l2 else 0
        sum = l1Value + l2Value + carryForward
        nodeValueInResult = sum % 10
        results.addAtTail(nodeValueInResult)
        carryForward = sum // 10
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return results

#Explabnation in the folder Addsol3


print("========================'Solution without resrved list ===============================")

#Given two numbers represented by two lists, write a function that returns the sum in the form of a linked list.
"""solution with explanation below the link"""
#https://www.geeksforgeeks.org/add-two-numbers-represented-by-linked-list/