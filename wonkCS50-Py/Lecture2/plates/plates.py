plate = input("Plate: ").lower().strip()
bet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
valid_marker = 1
def check():
    if valid_marker == 1:
        print("Valid")
    else:
        print("Invalid")

if 6 >= len(plate) >= 2:
    pass
else:
    valid_marker = 0

if len(plate) == 2 and plate[0:1].isalpha():
    pass
elif len(plate) == 3 and plate[2].isalnum() and plate[0:1].isalpha():
    pass
elif len(plate) == 4 and plate[0:2].isalpha() and plate[3].isnumeric():\
    pass
elif len(plate) == 4 and plate[0:1].isalpha() and plate[2:3].isnumeric():
    pass
elif len(plate) == 4 and plate[2] == "0":\
    valid_marker = 0
elif len(plate) == 5 and plate[0:1].isalpha() and plate [2:4].isnumeric():\
    pass
elif len(plate) == 5 and plate[0:2].isalpha() and plate[3:4].isnumeric():\
    pass
elif len(plate) == 5 and plate[0:3].isalpha() and plate[4].isnumeric():\
    pass
elif len(plate) == 6 and plate [0:1].isalpha() and plate[2:5].isnumeric():\
    pass
elif len(plate) == 6 and plate[0:2].isalpha() and plate[3:5].isnumeric():\
    pass
elif len(plate) == 6 and plate[0:3].isalpha() and plate[4:5].isnumeric():\
    pass
elif len(plate) == 6 and plate[0:4].isalpha() and plate[5].isnumeric():\
    pass
elif len(plate) == 6 and plate[0:5].isalpha():
    pass
else:
    valid_marker = 0

check()
