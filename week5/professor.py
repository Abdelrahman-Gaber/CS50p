import random


def main():
    level = get_level()
    x = [generate_integer(level) for _ in range(10)]
    y = [generate_integer(level) for _ in range(10)]
    user_score =  0
    for i in range(len(x)):
        counter = 0

        while counter != 3:
            try:
                answer = int(input(f'{x[i]} + {y[i]} = ')) 

                if answer == (x[i] + y[i]):
                    counter = 3
                    user_score += 1

                else:
                   raise ValueError
                    
            except ValueError:
                counter += 1
                print('EEE')
                if counter == 3:
                    print(f'{x[i]} + {y[i]} = {x[i] + y[i]}')

    print(f'Score: {user_score}')


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1,2,3]:
                raise ValueError
            else:
                return level
        except ValueError:
            print("Level must be in 1, 2, 3")


def generate_integer(level):
    try:
        if level == 1:
            return random.randint(1, 9)
        elif level == 2:
            return random.randint(1,99)
        elif level == 3:
            return random.randint(1,999)
        else:
            raise ValueError
    except ValueError:
        print("Level must be in 1, 2, 3")

if __name__ == "__main__":
    main()