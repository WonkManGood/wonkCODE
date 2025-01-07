mydict = {}

while True:
    try:
        item = input().upper()
        if item in mydict:
            mydict[item] = mydict[item] + 1
        else:
            mydict[item] = 1
    except EOFError:
        for i in mydict:
            print(mydict[i], i)
        break
