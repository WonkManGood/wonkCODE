import csv as c

# /// Validates you have cipher and returns it as a dictionary.
def open_cipher():
    try:
        cipher_open = open('./dictionary.csv', 'r')
        cipher = c.DictReader(cipher_open)
    except:
        raise(LookupError('Couldn\'t find cipher. Validate build with source and/or run program in build folder.'))
    
    wonkCIPHER = []
    for row in cipher:
        wonkCIPHER.append(row)
    return wonkCIPHER

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
    if len(i) > 25: raise ValueError("Length must be 1-25 characters.")
    placeholder = 0
    
                


def decrypt():
    ...
    # clear()
    # i = 0
    # for i in range(5):
    #     i = i + 1
    #     line = input(f'Enter line #{i}: ')
    #     wonkCIPHER.append(line)


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
