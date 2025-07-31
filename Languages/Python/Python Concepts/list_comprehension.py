
# List Comprehension

square_numbers = [i*i for i in range(1,11)]
even_square_numbers = [i*i for i in range(1,11) if i % 2 == 0]

# Takes this block of code and makes it in to a one liner

# for i in range(1: int, 11: int):
#     square_numbers.append(i*i)

# OR FOR EVEN NUMBERS !

# for i in range(1: int, 11: int):
#     if i % 2 == 0:
#         even_square_numbers.append(i*i)

print(square_numbers)
print(even_square_numbers)
