print("Welcome to the To-Do List")
print("Please type your name")
name = input(">")

print(f"Hello {name}, please type a task: ")
task = input(">")
count = 0
for number in range(count):
  count += 1
  print(task, number)

  command = ""
  while command.lower() != "quit":
    command = input(">")
    print("Program", command)

print(f"We have {count} tasks")
