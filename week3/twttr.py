'''
    Omit vowls in a given word lower or upper
    loop on the user input
    check if the lower of the letter is in the vowls list
    remove vowls and create the input again
'''


vowels = ["a", "e", "i", "o", "u"]
user_input = input("Input: ")
output = []

# Find a way to omit the vowel in the word
for char in user_input:
    if char not in vowels:
        output.append(char)

print(f"Output: {"".join(output)}")
