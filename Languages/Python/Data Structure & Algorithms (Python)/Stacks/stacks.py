""" Stacks """
# A linear data structure that follows LIFO (Last-In-First-Out) principle

# Push: Adds a new element on the stack.
# Pop: Removes and returns the top element from the stack.
# Peek: Returns the top (last) element on the stack.
# isEmpty: Checks if the stack is empty.
# Size: Finds the number of elements in the stack.

stack = []

# Push
stack.append('A')
stack.append('B')
stack.append('C')
print('Stack: ', stack)

# Peek
topElement = stack[-1]
print('Peek: ', topElement)

# Size before Pop
print('Size: ', len(stack))

# Pop
poppedElement = stack.pop()
print('Pop: ', poppedElement)

# Stack after Pop
print('Stack after Pop: ', stack)

# isEmpty
isEmpty = not bool(stack)
print('isEmpty: ', isEmpty)

# Size after Pop
print('Size: ', len(stack))

