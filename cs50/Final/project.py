import csv as c

# /// Validates you have cipher and returns it as a dictionary.
def open_cipher():
    try:
        cipher_open = open('./dictionary.csv', 'r')
        cipher = list(c.DictReader(cipher_open))
    except:
        raise(LookupError('Couldn\'t find cipher. Validate build with source and/or run program in build folder.'))
    
    return cipher

def main():
    wonkCIPHER = open_cipher()
    print(wonkCIPHER)


# /// Prompts user for usage of program and returns function's results.
    print('''
    wonkCIPHER: -- 0.1
    a simple visual cipher - inspired by randomart in recent ssh builds


    Encrypt String:    0
    Decrypt String:    1
    Generate Random:   2
    ''')
    
    choice = input("Choice (0-2): ")
    match choice:
        case '0':
            print(encrypt(input("Enter string: ")))
        case '1':
            print(decrypt())
        case '2':
            print(random())


def encrypt(i):
    clear()
    if len(i) > 25: raise ValueError("Length must be 1-25 characters.") # checks length
    cipher = open_cipher() # init cipher
    q = [] # placeholder for output
    for iterate in range(0, len(i)): # this loop took me like 2 hours to do for some reason, only to find out it was an issue with open_cipher :(
        for row in cipher:
            if i[iterate] == row['input']:
                q.append(row['output'])
    return str('').join(q)
    
                


def decrypt():
    clear()
    lines = []
    print('''
The following will ask you for the 5 lines
of your cipher. Please enter line by line. If
a line is empty, simply press enter.

          ''')
    for i in range(1, 6):
        line = input(f"Line {i}: ")
        lines.append(str(line))
    
    cipher = open_cipher()
    for iterate in range(len(i)):
        ...




def random():
    import random as r
    ...

# /// Used to keep terminal looking clean.
def clear():
    from os import system, name
    if name == 'nt': system('cls')
    else: system('clear')


if __name__ == "__main__":
    main()
