def main():
    user_input = str(input("Enter a string: "))
    print(convert(user_input))

def convert(user_input):
    return user_input.replace(":)", "🙂").replace(":(","🙁")

main()