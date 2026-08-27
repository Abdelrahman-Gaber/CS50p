def main():
    time = input("Enter time of the day: ")
    time = convert(time)

    if 7.00 <= time <= 8.00:
        print("breakfast time")
    elif 12.00 <= time <= 13.00:
        print("lunch time")
    elif 18.00 <= time <= 19.00:
        print("dinner time")


def convert(time):
    # split the time into hours and minutes
    hours, minutes = time.split(":")

    # format minutes to represent 0.5 as 30 minutes
    minutes = round(int(minutes) / 60, 2)

    return float(int(hours) + minutes)


if __name__ == "__main__":
    main()