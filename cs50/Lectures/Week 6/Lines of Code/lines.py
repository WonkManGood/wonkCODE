import sys

file = sys.argv[1]

def count(f):
    counter = 0
    with open(f, "r") as O:
        o = O.readlines()

        for line in o:
            line = line.strip()
            # print(line)
            if line == "" or line.startswith("#"):
                pass
            else:
                counter = (counter + 1)
    print(counter)



def main():
    if 2 == len(sys.argv):
        pass
    else:
        print("Too many arguments.")
        sys.exit(1)

    if file.endswith(".py"):
        count(file)
    else:
        print("Not a python file.")
        sys.exit(1)

main()
