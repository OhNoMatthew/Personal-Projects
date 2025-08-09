""" Hashtables """

# Step 1: Create an Empty List
my_list = [None, None, None, None, None, None, None, None, None, None]

# Step 2: Create a Hash Function
def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)

    return sum_of_chars % 10

print("'Bob' has hash code: ", hash_function('Bob'))

# Step 3: Inserting an Element
def add (name):
    index = hash_function(name)
    my_list[index] = name

add('Bob')
print(my_list)

add('Pete')
add('Jones')
add('Lisa')
add('Siri')
print(my_list)

# Step 4: Looking up a name
def contains(name):
    index = hash_function(name)
    return my_list[index] == name

print("'Pete' is in the Hash Table: ", contains('Pete'))

# Step 5: Handling collisions
my_list = [
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  []
]

# Rewrite add
def addNew(name):
    index = hash_function(name)
    my_list[index].append(name)

addNew('Bob')
addNew('Pete')
addNew('Jones')
addNew('Lisa')
addNew('Siri')
addNew('Stuart')
print(my_list)
