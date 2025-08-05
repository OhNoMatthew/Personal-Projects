""" Stacks with Classes """

# Memory Efficient: Array elements do not hold the next elements address like linked list nodes do.
# Easier to implement and understand: Using arrays to implement stacks require less code than using linked lists, and for this reason it is typically easier to understand as well.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self): 
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)

# Create a stack
myStack = Stack()

myStack.push('A')
myStack.push('B')
myStack.push('C')

print("Stack: ", myStack.stack)
print("Pop: ", myStack.pop())
print("Stack after Pop: ", myStack.stack)
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.size())
