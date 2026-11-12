import sys

count = 0
try: 
    if len(sys.argv) != 2 or sys.argv[1][-3:] != ".py":
        sys.exit()
    else:

        with open(sys.argv[1], "r") as file:
            for line in file:
                if line[0] != "#" and line.strip() != "":
                    count += 1

        print(f"Lines of code count in {sys.argv[1]} is {count}") 
except FileNotFoundError:
    sys.exit()