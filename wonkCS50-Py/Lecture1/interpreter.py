inp = input("Calc: ")
x, y, z = inp.split(" ", maxsplit=3)
x = float(x)
y = str(y)
z = float(z)
if y == "+":
    print(x + z, end="")
elif y == "-":
    print(x - z, end="")
elif y == "*":
    print(x * z, end="")
elif y == "/":
    print(x/z, end="")
else:
    print("Incorrect format.")
