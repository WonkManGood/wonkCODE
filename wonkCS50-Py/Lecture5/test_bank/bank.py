# def start(n):
#     str(n.startswith("H" or "h", int(1)))

# inp = str(input("Greeting: ")).lower().replace(" ", "")
# if inp == "hello":
#     print("$0")
# elif inp == "hello,newman":
#     print("$0")
# elif inp[0] == "h":
#     print("$20", end="")
# else:
#     print("$100")

####################################

def main():
    greeting = input("Greeting: ")
    print(value(greeting))

def value(greeting):
    greeting = greeting.lower().strip()
    if greeting == "hello":
        return 100
    elif greeting.startswith("h") or greeting.startswith("H"):
        return 20
    else:
        return 0


if __name__ == "__main__":
    main()
