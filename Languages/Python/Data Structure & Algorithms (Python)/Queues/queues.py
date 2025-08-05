""" Queues with Python """

# Enqueue: Adds a new element to the queue.
# Dequeue: Removes and returns the first (front) element form the queue.
# Peek: Returns the first element in the queue.
# isEmpty: Checks if the queue is empty
# Size: Finds the number of elements in the queue.

queue = []

# Enqueue
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue: ", queue)

# Peek
frontElement = queue[0]
print("Peek: ", frontElement)

# Dequeue
poppedElement = queue.pop(0)
print("Dequeue: ", poppedElement)

print("Queue after Dequeue: ", queue)

# isEmpty
isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)

# Size
print("Size: ", len(queue))
