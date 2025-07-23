a, b = 10, 15

try:
    print(a + b)
except TypeError as e:
    print("Please enter a valid number in the form of an integer or a float!")
except Exception as e: # Use as a last resort, Exception takes up all exceptions.
    print("Something else went wrong...")

print("Continuing with the program...")
