# while True:
#     try:
#         fuel = input("Fraction: ")
#         x, y = fuel.split("/")
#         x, y = int(x), int(y)
#         percent = (x/y)
#         percent = round(percent, 2)
#         percent = int(percent*100)
#         if 101 > percent >= 99:
#             print("F", end="")
#         elif 1 < percent < 99:
#             print((str(percent) + "%"), end="")
#         elif percent <= 1:
#             print("E", end="")
#         elif percent >= 101:
#             pass
#     except ValueError:
#         pass
#     except ZeroDivisionError:\
#         pass
#     else:
#         break



def main():
    print(gauge(convert(input("Fraction: "))))


def convert(fraction):
    try:
        a, b = str(fraction).split("/")
        if int(a) > int(b): raise ValueError
        else: a = round(int(a)/int(b)*100)
        return a
    except:
        if int(b) == 0: raise ZeroDivisionError
        else: raise ValueError

def gauge(percentage):
    if percentage == 0: return "E"
    elif percentage == 100: return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()

