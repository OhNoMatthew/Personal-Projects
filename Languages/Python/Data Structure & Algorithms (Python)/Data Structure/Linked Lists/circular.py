""" Circular Linked Lists """

# A circular linked list is like a singly or doubly linked list with the first node, the "head", and the last node, the "tail", connected.
# In singly or doubly linked lists, we can find the start and end of a list by just checking if the links are null.
# But for circular linked lists, more complex code is needed to explicitly check for start and end nodes in certain applications.

# Circular linked lists are good for lists you need to cycle through continuously.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """ Add Element """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")

cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.display()
