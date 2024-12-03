def shorten(x):
    shortened = []
    for vowel in x:
        if vowel not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            shortened.append(vowel)
    out = str("".join(shortened))
    return out

def main():
    text = input("Text: ")
    output = shorten(text)
    print("Output:", output)

if __name__ == "__main__":
    main()