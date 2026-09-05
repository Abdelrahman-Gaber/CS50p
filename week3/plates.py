import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Flag to keep track if the sequence already had a number appearing before
    # Important to check on letters after digits
    first_number = False

    ''' 
        Check on the main validations that eliminate a vanity plate must be 2 to 6 characters long 
        and the 1st 2 characters has to be string
    '''
    if 2 <= len(s) <=6 and s[0:1].isalpha():
        for char in s[2:]:
            if char in string.punctuation or not char.isalnum():
                 return False
            
            elif char.isalpha() and first_number is True:
                 return False

            elif char.isnumeric() and first_number is False and char != 0:
                if int(char) == 0:
                    return False
                else:
                    first_number = True


        return True
    else:
         return False


main()