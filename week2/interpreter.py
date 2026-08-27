user_input = input("enter the arithmatic expression: ")

x, y, z = user_input.split(" ")

match y:
    case "+":
        print(f"{(float(x) + float(z)):.1f}")
    case "/":
        print(f"{(float(x) / float(z)):.1f}")
    case "*":
        print(f"{(float(x) * float(z)):.1f}")
    case "-":
        print(f"{(float(x) - float(z)):.1f}")    