def main():
    user_input = input("What is the answer to life, the universe, and everything? ").lower()
    if deep_thought(user_input):
        print("Yes")
    else:
        print("No")

def deep_thought(user_input):
    return user_input == "42" or user_input == "forty-two" or user_input == "forty two"

main()