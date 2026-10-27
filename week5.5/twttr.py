def main():
    word = input("Input: ")
    print(shorten(word))

def shorten(word):
    for char in ['u', 'i', 'e', 'a', 'o', 'U', 'I', 'E', 'A', 'O']:
        word = word.replace(char, '')
    return word

if __name__ == "__main__":
    main()