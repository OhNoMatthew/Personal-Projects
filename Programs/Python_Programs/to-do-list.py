""" Simple To Do List """

# Create a node for data
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Main:

# Create a list
    print('Welcome to your To-Do List!')
    my_task: list = []

# Start the queue list
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

# Add a task
    def addTask(self, task):
        new_node = Node(task)
        if self.rear is None:
            self.front = self.rear = new_node
            self.length += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self += 1

# Delete a Task
    def deleteTask(self):
        if self.isEmpty():
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        return temp.data
    
# Check if the Task list is empty
    def isEmpty(self):
        print('Seems that the list is empty')
        return self.length == 0
    
# Mark a task as done
