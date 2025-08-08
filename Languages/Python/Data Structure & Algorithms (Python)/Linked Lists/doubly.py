""" Doubly Linked Lists """

# A doubly linked list has nodes with addresses to both the previous and the next node and therefore takes up more memory. 
# But doubly linked lists are good if you want to be able to move both up and down in the list.

class Node:
    """ Node Creation """
    def __init__(self, data):
        self.data = data # Store the data
        self.next = None # Pointer to the next node
        self.prev = None # Pointer to the previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """ Add Element """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def display_forward(self):
        """ Traverse Front """
        temp = self.head
        while temp:
            print(temp.data, end=" <-> " if temp.next else "\n")
            temp = temp.next
    
    def display_backward(self):
        """ Traverse Back """
        temp = self.head
        if not temp:
            return
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" <-> " if temp.prev else "\n")
            temp = temp.prev
           
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)

print("Forward Traversal:")
dll.display_forward()

print("Backward Traversal:")
dll.display_backward()
