"""Module providing a function printing python version."""

# indentations are very important when typing up certain operations/functions

#Chain Comparison Operators

# age should be between 18 and 65

age = 22

# Lines 8 and 9 are the same
# if age >= 18 and age < 65:
if 18 <= age < 65:
    print("Eligible")
    print("---")


#Loops

for number in range (1, 10, 2):
    print("Attempt", number, (number) * ".")

for number in range (1,4):
    print("Again", number, (number) * ".")

print("---")


#For .. Else

successful = True #Depending on the boolean statement it will attempt three times before printing out a message
for number in range (3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Unsuccessful")
print("---")


#Nested Loops
for x in range(5):
    for y in range (3):
        print(f"({x}, {y})")
print("---")


#Iterables

# print(type(5)) Int type
# print(type(range(5))) Range type

# for y in [1,2,3,4]:
#     print(y)

for x in "Python":
    print(x)
print("---")


#While Loops, While loops are used for infinite loops. For loops are considered to use for finite loops
number = 100
while number > 0:
    print(number)
    number //= 2

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)
print("---")


#Infinite Loop
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
