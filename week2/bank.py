user_input = input("Give me your best greeting: ")[0:5].lower()

if user_input == "hello":
    print("$0")
elif user_input[0] == "h":
    print("$20")
else:
    print("$100")