import emoji

while True:
    try:
        inp = input("").lower()
        if inp == ":thumbsup:":
            inp = ":thumbs_up:"
        elif inp == "hello, :earth_asia:":
            print("hello, 🌏")
        print(emoji.emojize(inp))
        break
    except:
        pass
