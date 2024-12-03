from datetime import date
from sys import exit
import operator


def main():
    dates = input("Date: ")
    try: a, b, c = str(dates).split("-")
    except:
        print("Incorrect format.")
        exit(0)
    
    print(inflect(dates))



def inflect(n):
    import inflect as i
    i = i.engine()
    today = date.today()

    difference = operator.sub(today, date.fromisoformat(n))
    return i.number_to_words

if __name__ == "__main__":
    main()
