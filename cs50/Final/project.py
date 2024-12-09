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
            encrypt(input("Enter string: "))
        case '1':
            decrypt()
        case '2':
            print(random())


def encrypt(i):
    clear()
    if 0 < len(i) > 25: raise ValueError("Length must be 1-25 characters.") # checks length
    cipher = open_cipher() # init cipher
    q = [] # placeholder for output
    for iterate in range(0, len(i)): # this loop took me like 2 hours to do for some reason, only to find out it was an issue with open_cipher :(
        for row in cipher:
            if i[iterate] == row['input']:
                q.append(row['output'])
    i = str('').join(q)

    box_length = (14)
    print(f'┌' + ('─' * box_length) + '┐')
    if len(i) <= 10:
        box_length = (len(i) + 4)
        difference = (10 - len(i))
        print(f'│  '+ i + (difference * ' ') + '  │')
        for _ in range(4):
            print(f'│' + (' ' * (box_length + difference)) + '│')
        print(f'└' + ('─' * (box_length + difference) + '┘'))#                                  } there was probably a better way to do this, but my brain couldnt figure it without more packages
    elif 10 < len(i) <= 20:
        difference = (20 - len(i))
        print(f'│  ' + i[0:10] + '  │')
        print(f'│  ' + i[10:] + (difference * ' ') + '  │')
        for _ in range(3):
            print(f'│' + (' ' * (box_length)) + '│')
        print(f'└' + ('─' * box_length) + '┘')
    elif 20 < len(i) <= 30:
        difference = (30 - len(i))
        print(f'│  ' + i[0:10] + '  │')
        print(f'│  ' + i[10:20] + '  │')
        print(f'│  ' + i[20:] + (difference * ' ') + '  │')
        for _ in range(2):
            print(f'│' + (' ' * (box_length)) + '│')
        print(f'└' + ('─' * box_length) + '┘')
    elif 30 < len(i) <= 40:
        difference = (40 - len(i))
        print(f'│  ' + i[0:10] + '  │')
        print(f'│  ' + i[10:20] + '  │')
        print(f'│  ' + i[20:30] + '  │')
        print(f'│  ' + i[30:] + (difference * ' ') + '  │')
        for _ in range(1):
            print(f'│' + (' ' * (box_length)) + '│')
        print(f'└' + ('─' * box_length) + '┘')
    elif 40 < len(i) <= 50:
        difference = (40 - len(i))
        print(f'│  ' + i[0:10] + '  │')
        print(f'│  ' + i[10:20] + '  │')
        print(f'│  ' + i[20:30] + '  │')
        print(f'│  ' + i[30:40] + '  │')
        print(f'│  ' + i[40:] + (difference * ' ') + '  │')
        print(f'└' + ('─' * box_length) + '┘')
    print('   wonkCIPHER\n')

                


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
    placeholder = 0
    for line in lines:
        if len(line) % 2 == 0:
            for iter in len(line):
                
        else: continue




def random():
    import random as r
    # if len(i) <= 10:
    #     box_length = (len(i) + 4)
    #     difference = (10 - len(i))
    #     print(f'│  '+ i + (difference * ' ') + '  │')
    #     for _ in range(4):
    #         print(f'│' + (' ' * (box_length + difference)) + '│')
    #     print(f'└' + ('─' * (box_length + difference) + '┘'))
    # elif 10 < len(i) <= 20:
    #     difference = (20 - len(i))
    #     print(f'│  ' + i[0:10] + '  │')
    #     print(f'│  ' + i[10:] + (difference * ' ') + '  │')
    #     for _ in range(3):
    #         print(f'│' + (' ' * (box_length)) + '│')
    #     print(f'└' + ('─' * box_length) + '┘')
    # elif 20 < len(i) <= 30:
    #     difference = (30 - len(i))
    #     print(f'│  ' + i[0:10] + '  │')
    #     print(f'│  ' + i[10:20] + '  │')
    #     print(f'│  ' + i[20:] + (difference * ' ') + '  │')
    #     for _ in range(2):
    #         print(f'│' + (' ' * (box_length)) + '│')
    #     print(f'└' + ('─' * box_length) + '┘')
    # elif 30 < len(i) <= 40:
    #     difference = (40 - len(i))
    #     print(f'│  ' + i[0:10] + '  │')
    #     print(f'│  ' + i[10:20] + '  │')
    #     print(f'│  ' + i[20:30] + '  │')
    #     print(f'│  ' + i[30:] + (difference * ' ') + '  │')
    #     for _ in range(1):
    #         print(f'│' + (' ' * (box_length)) + '│')
    #     print(f'└' + ('─' * box_length) + '┘')
    # elif 40 < len(i) <= 50:
    #     difference = (40 - len(i))
    #     print(f'│  ' + i[0:10] + '  │')
    #     print(f'│  ' + i[10:20] + '  │')
    #     print(f'│  ' + i[20:30] + '  │')
    #     print(f'│  ' + i[30:40] + '  │')
    #     print(f'│  ' + i[40:] + (difference * ' ') + '  │')
    #     print(f'└' + ('─' * box_length) + '┘')
    # print('   wonkCIPHER\n')

# /// Used to keep terminal looking clean.
def clear():
    from os import system, name
    if name == 'nt': system('cls')
    else: system('clear')


if __name__ == "__main__":
    main()
