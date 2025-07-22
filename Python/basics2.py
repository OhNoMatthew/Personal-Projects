"""Module providing a function printing python version."""

#Conditional Statment
temperature = 15

if temperature > 30:
    print("It's warm")
    print("Drink water")

# else if
elif temperature > 20:
    print("It's nice")

else:
    print("It's cold")

print("Done")
print("---")


#Ternary Condition

age = 17

#This code works but there are cleaner options
# if age >= 18:
#     message = "Eligible"
# else:
#     message = "Not Eligible"

message = "Eligible" if age >= 18 else "Not Eligible"
print(message)
print("---")


#Logical Operators
#and or not

high_income = True
good_credit = True
student = True

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")
print("---")




