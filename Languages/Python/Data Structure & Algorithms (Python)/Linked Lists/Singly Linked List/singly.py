""" Singly Linked Lists """

# A singly linked list is the simplest kind of linked lists. It takes up less spae in memory because each node has only one address to the next node.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    """ Traverse """
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traverseAndPrint(node1)
