def main():
    fraction = input('Input: ')
    print(gauge(convert(fraction)))


def convert(fraction):

    x, y = int(fraction.split('/')[0]), int(fraction.split('/')[1])
    if x < 0 or y < 0 or x > y:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    return (round(x/y * 100))

def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()