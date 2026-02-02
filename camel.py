camel_case = input("Write in Camel Case: ")

print("snake_case: ", end="")

for char in camel_case:
    if char.isupper():
        print("_" + char.lower(), end="")
    else:
        print(char, end="")

print()