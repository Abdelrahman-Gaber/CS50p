import csv
import sys


field_names = ["first", "last", "house"]

try:
    if len(sys.argv) > 3:
        sys.exit("Too many commend-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            with open(sys.argv[2], "w") as file2:
                writer = csv.DictWriter(file2, fieldnames=field_names)
                writer.writeheader()
                for row in reader:
                    last, first = row["name"].split(sep= ", ")
                    writer.writerow({"first": first, "last": last, "house": row["house"]})

except FileNotFoundError:
    sys.exit(f"couldn't read {sys.argv[1]}")