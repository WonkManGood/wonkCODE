while True:
    try:
        fuel = input("Fraction: ")
        x, y = fuel.split("/")
        x, y = int(x), int(y)
        percent = (x/y)
        percent = round(percent, 2)
        percent = int(percent*100)
        if 101 > percent >= 99:
            print("F", end="")
        elif 1 < percent < 99:
            print((str(percent) + "%"), end="")
        elif percent <= 1:
            print("E", end="")
        elif percent >= 101:
            pass
    except ValueError:
        pass
    except ZeroDivisionError:\
        pass
    else:
        break
