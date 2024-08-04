#Description of the problem 
# https://leetcode.com/problems/linked-list-cycle-ii/description/
# https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/31200384#overview
 





# Solution N*1:
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
def checkLoop(head):
    
    # The while loop runs at most 'n' times where 'n' is the number of elements in the linked list. 
    # Thus, the time complexity is O(n).
    
    if not head or not head.next:
        return None
 
    hare = head
    tortoise = head
    while hare and hare.next:
        hare = hare.next.next
        tortoise = tortoise.next
        if hare == tortoise:
            break
 
    if hare != tortoise:
        return None
 
    # find where cycle begins
    pointer = head
    while pointer != tortoise:
        pointer = pointer.next
        tortoise = tortoise.next
 
    return tortoise

# For Testing
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
 
one.next = two
two.next = three
three.next = four
four.next = five
five.next = six
# make a loop
six.next = three
 
head = one
 
print(checkLoop(head).value)

#Explanation in the folder : Cycle1


#Solution N°2:
"""this solution the same in the top but here without detection cycle 
   the diff between sol1 and sol 2 it the line 57 and the line 100  """
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
def checkLoop(head):
    if not head or not head.next:
        return None
 
    hare = head
    tortoise = head
    while hare and hare.next:
        hare = hare.next.next
        tortoise = tortoise.next
        if hare == tortoise:
            break
 
    if hare != tortoise:
        return None
 
    # find where cycle begins
    pointer = head
    while pointer != tortoise:
        pointer = pointer.next
        tortoise = tortoise.next
 
    return tortoise

# For Testing (No Loop)
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
 
one.next = two
two.next = three
three.next = four
four.next = five
five.next = six
# No loop, six.next is None by default

head = one

# Expecting "No cycle detected" as output
cycle_node = checkLoop(head)
if cycle_node:
    print(f"Cycle detected at node with value: {cycle_node.value}")
else:
    print("No cycle detected")







print("================================================================================================")


#Solution N3:
"""#Without test"""
class Solution:
  def detectCycle(self, head: ListNode) -> ListNode:
    # Initialize two pointers, slow and fast, to the head of the linked list.
    slow = head
    fast = head

    # Move the slow pointer one step and the fast pointer two steps at a time through the linked list,
    # until they either meet or the fast pointer reaches the end of the list.
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        # If the pointers meet, there is a cycle in the linked list.
        # Reset the slow pointer to the head of the linked list, and move both pointers one step at a time
        # until they meet again. The node where they meet is the starting point of the cycle.
        slow = head
        while slow != fast:
          slow = slow.next
          fast = fast.next
        return slow

    # If the fast pointer reaches the end of the list without meeting the slow pointer,
    # there is no cycle in the linked list. Return None.
    return None 
  

#Explanation in the folder : Cycle3




#Solution N*4
"""with tes
   the same code in sol3 but with adding the code necessary to test thei code 
   we have in this code two test in one hand  for cycle detecte and on the othefr hand for No cycle detecttion  """

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None

# Example with a cycle
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)
six = ListNode(6)

one.next = two
two.next = three
three.next = four
four.next = five
five.next = six
six.next = three  # Create a cycle

solution = Solution()
cycle_node = solution.detectCycle(one)
if cycle_node:
    print(f"Cycle detected at node with value: {cycle_node.val}")
else:
    print("No cycle detected")

# Example without a cycle
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)
six = ListNode(6)

one.next = two
two.next = three
three.next = four
four.next = five
five.next = six
# No cycle

solution = Solution()
cycle_node = solution.detectCycle(one)
if cycle_node:
    print(f"Cycle detected at node with value: {cycle_node.val}")
else:
    print("No cycle detected")





#More solution in this link:: https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/

















