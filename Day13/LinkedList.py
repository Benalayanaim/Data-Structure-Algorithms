#Description Problem 
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/30734978#overview
#https://leetcode.com/problems/design-linked-list/description/

#Undrestand how the problem work 

#Class Syntax
#https://www.geeksforgeeks.org/python-classes-and-objects/




#Solution N°1:
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1

        current = self.head

        for _ in range(0, index):
            current = current.next

        return current.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be
        the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked
        list, the node will be appended to the end of linked list. If index is greater than the length, the node will not
        be inserted.
        """
        if index > self.size:
            return

        current = self.head
        new_node = ListNode(val)

        if index <= 0:
            new_node.next = current
            self.head = new_node
        else:
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return

        current = self.head

        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(0, index - 1):
                current = current.next
            current.next = current.next.next

        self.size -= 1


# Create the linked list
linked_list = MyLinkedList()

# Add elements at the head
linked_list.addAtHead(1)  # List is now [1]
linked_list.addAtHead(2)  # List is now [2, 1]

# Add elements at the tail
linked_list.addAtTail(3)  # List is now [2, 1, 3]
linked_list.addAtTail(4)  # List is now [2, 1, 3, 4]

# Add elements at specific index
linked_list.addAtIndex(2, 5)  # List is now [2, 1, 5, 3, 4]
linked_list.addAtIndex(0, 6)  # List is now [6, 2, 1, 5, 3, 4]

# Get values
print(linked_list.get(0))  # Output: 6
print(linked_list.get(2))  # Output: 1
print(linked_list.get(5))  # Output: 4
print(linked_list.get(6))  # Output: -1 (invalid index)

# Delete elements at specific index
linked_list.deleteAtIndex(0)  # List is now [2, 1, 5, 3, 4]
linked_list.deleteAtIndex(2)  # List is now [2, 1, 3, 4]
linked_list.deleteAtIndex(3)  # List is now [2, 1, 3]
linked_list.deleteAtIndex(3)  # No change, index is invalid
linked_list.deleteAtIndex(1)  # List is now [2, 3]

# Check final list values by getting them one by one
print([linked_list.get(i) for i in range(linked_list.size)])  # Output: [2, 3]



"""Expected Output:
After linked_list.addAtHead(1): List is [1]
After linked_list.addAtHead(2): List is [2, 1]
After linked_list.addAtTail(3): List is [2, 1, 3]
After linked_list.addAtTail(4): List is [2, 1, 3, 4]
After linked_list.addAtIndex(2, 5): List is [2, 1, 5, 3, 4]
After linked_list.addAtIndex(0, 6): List is [6, 2, 1, 5, 3, 4]
linked_list.get(0): 6
linked_list.get(2): 1
linked_list.get(5): 4
linked_list.get(6): -1 (invalid index)
After linked_list.deleteAtIndex(0): List is [2, 1, 5, 3, 4]
After linked_list.deleteAtIndex(2): List is [2, 1, 3, 4]
After linked_list.deleteAtIndex(3): List is [2, 1, 3]
After linked_list.deleteAtIndex(3): List is [2, 1, 3] (no change, invalid index)
After linked_list.deleteAtIndex(1): List is [2, 3]
Final list values: [2, 3]
"""




print("============================================================")





#Solution N°2:
# Create a Node class to create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a node at begin of LL
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    # Method to add a node at any index
    # Indexing starts from 0.
    def insertAtIndex(self, data, index):
        if (index == 0):
            self.insertAtBegin(data)
            
        position = 0
        current_node = self.head
        while (current_node != None and position+1 != index):
            position = position+1
            current_node = current_node.next

        if current_node != None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

    # Method to add a node at the end of LL
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node

    # Update node of a linked list
        # at given position
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while(current_node != None and position != index):
                position = position+1
                current_node = current_node.next

            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")

    # Method to remove first node of linked list

    def remove_first_node(self):
        if(self.head == None):
            return

        self.head = self.head.next

    # Method to remove last node of linked list
    def remove_last_node(self):

        if self.head is None:
            return

        current_node = self.head
        while(current_node != None and current_node.next.next != None):
            current_node = current_node.next

        current_node.next = None

    # Method to remove at given index
    def remove_at_index(self, index):
        if self.head == None:
            return

        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next

            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")

    # Method to remove a node from linked list
    def remove_node(self, data):
        current_node = self.head

        if current_node.data == data:
            self.remove_first_node()
            return

        while(current_node != None and current_node.next.data != data):
            current_node = current_node.next

        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next

    # Print the size of linked list
    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0

    # print method for the linked list
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next


# create a new linked list
llist = LinkedList()

# add nodes to the linked list
llist.insertAtEnd('a')
llist.insertAtEnd('b')
llist.insertAtBegin('c')
llist.insertAtEnd('d')
llist.insertAtIndex('g', 2)

# print the linked list
print("Node Data")
llist.printLL()

# remove a nodes from the linked list
print("\nRemove First Node")
llist.remove_first_node()
print("Remove Last Node")
llist.remove_last_node()
print("Remove Node at Index 1")
llist.remove_at_index(1)

# print the linked list again
print("\nLinked list after removing a node:")
llist.printLL()

print("\nUpdate node Value")
llist.updateNode('z', 0)
llist.printLL()

print("\nSize of linked list :", end=" ")
print(llist.sizeOfLL())

#Explanation

"""
Explanation of Example Usage
Creating the Linked List: Initializes an empty linked list.
Adding Nodes:
insertAtEnd('a'): Adds 'a' to the end.
insertAtEnd('b'): Adds 'b' to the end.
insertAtBegin('c'): Adds 'c' to the beginning.
insertAtEnd('d'): Adds 'd' to the end.
insertAtIndex('g', 2): Inserts 'g' at index 2.
Printing the Linked List: Prints all the nodes.
Removing Nodes:
remove_first_node(): Removes the first node.
remove_last_node(): Removes the last node.
remove_at_index(1): Removes the node at index 1.
Updating a Node: Updates the value of the node at index 0 to 'z'.
Size of the Linked List: Prints the size of the linked list.

"""




print("============================================================")


#Solution N°3
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
 
    # Time Complexity: O(n) as we might traverse through the entire list in the worst case
    # Space Complexity: O(1) as no additional space is required
    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
 
        counter = 0
        current = self.head
        while counter != index:
            current = current.next
            counter += 1
        return current
 
    # Time Complexity: O(1) as we perform constant time operations
    # Space Complexity: O(1) as no additional space is required
    def addAtHead(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1
 
    # Time Complexity: O(1) as we perform constant time operations
    # Space Complexity: O(1) as no additional space is required
    def addAtTail(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
 
    # Time Complexity: O(n) as we might traverse through the entire list in the worst case
    # Space Complexity: O(1) as no additional space is required
    def addAtIndex(self, index, value):
        if index < 0 or index > self.size:
            return 'invalid index'
        if index == self.size:
            return self.addAtTail(value)
        if index == 0:
            return self.addAtHead(value)
        node = Node(value)
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = node
        node.next = temp
        self.size += 1
 
    # Time Complexity: O(n) as we might traverse through the entire list in the worst case
    # Space Complexity: O(1) as no additional space is required
    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return 'invalid index'
        if index == 0:
            temp = self.head
            self.head = temp.next
            self.size -= 1
            if self.size == 0:
                self.tail = None
            return temp.value
        if index == self.size - 1:
            old_tail = self.tail
            new_tail = self.get(index - 1)
            self.tail = new_tail
            new_tail.next = None
            self.size -= 1
            return old_tail.value
        prev = self.get(index - 1)
        deleted_node = prev.next
        prev.next = deleted_node.next
        self.size -= 1
        return deleted_node.value
    
# Initialize a new singly linked list
linked_list = SinglyLinkedList()

# Add elements at the head
linked_list.addAtHead(1)   # List is now [1]
linked_list.addAtHead(2)   # List is now [2, 1]

# Add elements at the tail
linked_list.addAtTail(3)   # List is now [2, 1, 3]
linked_list.addAtTail(4)   # List is now [2, 1, 3, 4]

# Add elements at specific indexes
linked_list.addAtIndex(2, 5)  # List is now [2, 1, 5, 3, 4]
linked_list.addAtIndex(0, 6)  # List is now [6, 2, 1, 5, 3, 4]

# Get values at specific indexes
print(linked_list.get(0).value)  # Output: 6
print(linked_list.get(2).value)  # Output: 1
print(linked_list.get(5).value)  # Output: 4
print(linked_list.get(6))        # Output: -1 (invalid index)

# Delete elements at specific indexes
linked_list.deleteAtIndex(0)  # List is now [2, 1, 5, 3, 4]
linked_list.deleteAtIndex(2)  # List is now [2, 1, 3, 4]
linked_list.deleteAtIndex(3)  # List is now [2, 1, 3]

# Print the size of the linked list
print(linked_list.size)  # Output: 3

# Print the values of the linked list
current = linked_list.head
while current:
    print(current.value, end=" ")  # Output: 2 1 3
    current = current.next


