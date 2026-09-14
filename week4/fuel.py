while True:
    try:
        fraction = input("Fraction: ")
        X = int(fraction.split("/")[0])
        Y = int(fraction.split("/")[1])
        percentage = int((X/Y)*100)
        if X > 0 and Y > 0 and X <= Y:
            if 1 < percentage < 99:
                print(f"{percentage}%")
                break
            elif percentage <= 1:
                print("E")
                break
            else:
                print("F")
                break
        else:
            pass
    except ValueError or ZeroDivisionError:
        pass

