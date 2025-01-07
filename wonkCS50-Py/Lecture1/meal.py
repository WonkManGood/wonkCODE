def main():
    inp = input("What time is it?: ")
    times = convert(inp)
    if 7 <= times <= 8:
        print("breakfast time", end="")
    elif 12 <= times <= 13:
        print("lunch time", end="")
    elif 18 <= times <= 19:
        print("dinner time", end="")
    else:
        print("error")


def convert(time):
    hours1, min1 = time.split(":")
    min = float(min1)/60
    hours = float(hours1)
    t = hours + min
    return t


if __name__ == "__main__":
    main()
