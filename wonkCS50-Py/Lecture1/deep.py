ans1 = str(input("What is the Answer to the Great QUestion of Life, the Universe, and Everything? "))
ans = str(ans1.strip().lower())
if ans == "42":
    print("Yes")
elif ans == "forty-two":
    print("Yes")
elif ans == "forty two":
    print("Yes")
else:
    print("No", end="")
