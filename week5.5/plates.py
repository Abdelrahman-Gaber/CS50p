import string

def main():
    plate = input('Plate: ')
    if isvalid(plate):
        print('Valid')
    else:
        print('Invalid')

def is_valid(s):
    first_number = False
    if 2 <= len(s) <= 6 and s[0:2].isalpha():
        for char in s[2:]:
            if char in string.punctuation:
                return False
            elif char.isalpha() and first_number == True: 
                return False
            elif char.isnumeric():
                if int(char) == 0 and first_number == False:
                    return False
                else:
                    first_number =  True
        return True
    else:
        return False

if __name__ == "__main__":
    main()