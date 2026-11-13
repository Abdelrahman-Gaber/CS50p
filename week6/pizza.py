import csv
import sys
from tabulate import tabulate

table_list = []
try:
    if len(sys.argv) != 2 or sys.argv[1][-4:] != ".csv":
        sys.exit()
    else:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                table_list.append(row)

            print(tabulate(table_list,headers="keys",tablefmt="grid"))

except FileNotFoundError:
    sys.exit()