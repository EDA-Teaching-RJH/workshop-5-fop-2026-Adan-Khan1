camel_case = input("Write in Camel Case: ")

print("snake_case: ", end="")

for char in camel_case:
    if char.isupper():
        # Print an underscore and the lowercase version of the letter
        print("_" + char.lower(), end="")
    else:
        print(char, end="")

mcamel_case = input("camelCase: ")

print("snake_case: ", end="")

for char in camel_case:
    if char.isupper():
        # Print an underscore and the lowercase version of the letter
        print("_" + char.lower(), end="")
    else:
        print(char, end="")

print()