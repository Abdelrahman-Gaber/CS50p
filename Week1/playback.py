def main():
    user_input = input("Enter a string: ")
    playback(user_input)

def playback(user_input):
    print(user_input.replace(" ", "..."))

main()