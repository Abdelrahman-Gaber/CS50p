groceries = {}

while True:
    try:
        item = input()
        if item.strip() != "":
            groceries[item.upper().strip()] += 1
        else:
            pass
    except KeyError:
        groceries[item.upper()] = 1
    except EOFError:
        break

for key in list(groceries.keys()):
    print(f"{groceries[key]} {key}")