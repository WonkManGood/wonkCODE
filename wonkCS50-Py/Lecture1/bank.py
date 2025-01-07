def start(n):
    str(n.startswith("H" or "h", int(1)))

inp = str(input("Greeting: ")).lower().replace(" ", "")
if inp == "hello":
    print("$0")
elif inp == "hello,newman":
    print("$0")
elif inp[0] == "h":
    print("$20", end="")
else:
    print("$100")
