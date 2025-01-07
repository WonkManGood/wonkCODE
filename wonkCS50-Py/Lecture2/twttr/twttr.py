inp = input(str("Input: "))
for vowel in inp:
    if vowel in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        print("", end="")
    else:
        print(vowel, end="")
print("")
    