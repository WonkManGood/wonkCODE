months = [
    {"1": "January", "January": "01"},
    {"2": "February", "February": "02"},
    {"3": "March", "March": "03"},
    {"4": "April", "April": "04"},
    {"5": "May", "May": "05"},
    {"6": "June", "June": "06"},
    {"7": "July", "July": "07"},
    {"8": "August", "August": "08"},
    {"9": "September", "September": "09"},
    {"10": "October", "October": "10"},
    {"11": "November", "November": "11"},
    {"12": "December", "December": "12"}
]
imonth = ""
idate = ""
iyear = ""
inp = ""
inp = str(input("Date: ")).strip()
if inp.count("/") > 0:
    inp = inp.replace(",", "")
    imonth, idate, iyear = inp.split("/")
if inp.count(" ") > 0:
    inp = inp.replace(",", "")
    imonth, idate, iyear = inp.split(" ")

idate = str(idate).zfill(2)

def alpha_to_dict(inp):
    for n, a in months:
        if inp == a:
            inp = n
            return inp

def numeric_to_dict(inp):
    inp = inp.zfill(2)
    return inp

if len(iyear) == 4:
    pass
else:
    print("Incorrect year format. Try ####")

if imonth.isalpha():
    imonth = alpha_to_dict(imonth)
    imonth = str(imonth).zfill(2)
elif imonth.isnumeric():
    numeric_to_dict(imonth)
    imonth = str(imonth).zfill(2)
else:
    print("failed line 42")

if 0 < int(imonth) < 13 and 0 < int(idate) < 32:
    print(f"{iyear}-{imonth}-{idate}")
else:
    inp = str(input("Date: ")).strip()

# its better
