import csv as c
from io import StringIO

def main():

# /// Validates you have cipher.
    try: cipher = c.reader(open('dictionary.csv', 'r'))
    except: raise(LookupError('Couldn\'t find cipher. Validate build and run program in build folder.'))

    print('''
    wonkCIPHER: -- 0.1
    a simple visual cipher


    Encrypt String:    0
    Decrypt String:    1
    Generate Random:   2
    ''')
    choice = input("Choice (0-2): ")


def encrypt():
    ...


def decrypt():
    ...


def random():
    import random as r
    ...


if __name__ == "__main__":
    main()
