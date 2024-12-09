# Method 1: Using a for loop (most Pythonic way)
print("Method 1: Using a for loop")
with open('input.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes trailing newline characters

# Method 2: Using .readlines()
print("\nMethod 2: Using .readlines()")
with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

# Method 3: Using .readline()
print("\nMethod 3: Using .readline()")
with open('input.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()

# Method 4: List comprehension
print("\nMethod 4: List comprehension")
lines = [line.strip() for line in open('input.txt', 'r')]
print(lines)
