# Camel case is the first word intial in lower case then supsequent words in uppercase
'''
    What can  I do?

    Get the user input
    run a for loop finding each letter in the input
    append all lower case letters to a variable initialized before the loop
    if a letter is capital then I append a _ and then the letter in lower case
'''

camel_case_input = input('camelCase: ')

snake_case = ""

for char in camel_case_input:
    if char.isupper():
        snake_case += "_" + char.lower()

    else:
        snake_case += char

print(f"snake_case: {snake_case}")
