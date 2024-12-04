from datetime import date
from sys import exit
import operator


def main():
    dates = input("Date: ")    
    print(inflect(dates))



def inflect(n):
    try: a, b, c = str(n).split("-")
    except:
        print("Incorrect format.")
        exit(1)

    import inflect as i
    i = i.engine()
    today = date.today()

    try: difference = operator.sub(today, date.fromisoformat(n))
    except:
        print("Incorrect ISO format.")
        exit(1)
    days = int(difference.days) * 24 * 60
    return f'{i.number_to_words(days, andword="").capitalize()} minutes'

if __name__ == "__main__":
    main()
