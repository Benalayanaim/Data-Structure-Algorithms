#Description For the Problem 
#





#Solution N°1:
class Node(object):
    """
    This is a Node class.
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert_node(self, data):
        """
        :param data: Node data
        :return: None
        """
        node = Node(data)
        node.next = self.head
        self.head = node

    def display_list(self):

        current = self.head
        while current:
            print(current.value, end="->")
            current = current.next

    def delete_duplicates(self):

        current = self.head
        # This is require to keep track of the prev Node
        prev = None
        duplicate_dict = dict()
        while current:
            if current.value not in duplicate_dict:
                duplicate_dict[current.value] = None
                # Track the prev Node
                prev = current
            else:
                # When a duplicate is found assign prev Node's next to current's next
                prev.next = current.next

            current = current.next

    def delete_duplicates_2(self):

        current = self.head

        while current:
            runner = current
            # Check until runner.next is not None.
            while runner.next:
                if current.value == runner.next.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next




l = LinkedList()
l.insert_node(25)
l.insert_node(35)
l.insert_node(15)
l.insert_node(32)
l.insert_node(25)
l.insert_node(80)
l.insert_node(15)
l.display_list()
#l.delete_duplicates()
l.delete_duplicates_2()
print()
l.display_list()


#Explanation 
#Explanation in the Folder
#below another explanation for thus code 
#https://python.plainenglish.io/deleting-duplicates-from-a-linked-list-in-python-69abe8149697




"""Another Solution found in this REFERENCE
====> : https://www.geeksforgeeks.org/python-program-for-removing-duplicates-from-an-unsorted-linked-list/"""



print("====================================================================================")


#Solution N2:
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

# Creating the list
head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node('a')
head.next.next.next.next.next = Node('a')

def display_list(head):
    current = head
    while current:
        print(current.val, end="->" if current.next else "\n")
        current = current.next

def removeDupes(head):
    
    # where n is the number of nodes in the linked list.
    
    curr = head
    while curr:
        nextDistinctVal = curr.next
        while nextDistinctVal is not None and curr.val == nextDistinctVal.val:
            nextDistinctVal = nextDistinctVal.next
        curr.next = nextDistinctVal
        curr = nextDistinctVal
    return head


# Display the list before removing duplicates
print("Before removing duplicates:")
display_list(head)

# Remove duplicates
removeDupes(head)

# Display the list after removing duplicates
print("After removing duplicates:")
display_list(head)


#The Explanation in Folder RemoveSol2