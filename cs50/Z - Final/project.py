# /// Globally initializes my attempt at a package.
try:
    import wonkCSV
    c = wonkCSV.wonkCSV
except: raise ModuleNotFoundError("Missing wonkCSV. Please validate build with source.")

# /// Initializes global placeholder for cipher lines.
wonkCIPHER = []

def main():

# /// Validates you have cipher.
    try: cipher = c.wonkCSV('dictionary.csv')
    except: raise(LookupError('Couldn\'t find cipher. Validate build with source and/or run program in build folder.'))

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


def encrypt():
    ...


def decrypt():
    clear()
    i = 0
    for i in range(5):
        i = i + 1
        line = input(f'Enter line #{i}: ')
        wonkCIPHER.append(line)


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
