import sys
import tabulate
import csv

if len(sys.argv) != 2:
    sys.exit(1)

while True:
    try:
        file = sys.argv[1]
        print(file)
        if file.endswith(".csv"):
            print(tabulate.tabulate(csv.reader(open(file)), headers="firstrow", tablefmt="grid"))
            break
        else:
            print("elsed")
            sys.exit(1)
    except IndexError:
        print("Usage: python3 pizza.py file.csv")
        sys.exit(1)
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)
