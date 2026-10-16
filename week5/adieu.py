import inflect

p = inflect.engine()

list_of_names = []
while True:
    try:
        name = input("Name: ")
        list_of_names.append(name)
    except EOFError:
        break

print(f"Adieu, adieu, to " + p.join(list_of_names))