""" import random

def level1():
    for i in range(10):
        r1 = random.randrange(0, 10)
        r2 = random.randrange(0, 10)
        while True:
            ans = input(f'{r2} + {r1} = ')
            ans = int(ans)
            real_ans = r1+r2
            if real_ans == ans:
                break
            else:
                print("EEE")

def level2():
    for i in range(10):
        r1 = random.randrange(10, 99)
        r2 = random.randrange(10, 99)
        while True:
            ans = input(f'{r2} + {r1} = ')
            ans = int(ans)
            real_ans = r1+r2
            if real_ans == ans:
                break
            else:
                print("EEE")

def level3():
    for i in range(10):
        r1 = random.randrange(100, 999)
        r2 = random.randrange(100, 999)
        while True:
            ans = input(f'{r2} + {r1} = ')
            ans = int(ans)
            real_ans = r1+r2
            if real_ans == ans:
                break
            else:
                print("EEE")

def get_level():
    while True:
        level = str(input("Level: "))
        if level == "1":
            level1()
            break
        if level == "2":
            level2()
            break
        if level == "3":
            level3()
            break
        else:
            print("Incorrect level. Pick 1-3")

get_level() """
# ^^^
# this was my original, but the fucking check50 wasnt accepting it despite it working nearly 1/1 as the example

import random
def main():
    lvl = get_level()
    count = 0
    for _ in range(10):
        i = 3
        while(i>0):
            if i==3:
                x = generate_integer(lvl)
                y = generate_integer(lvl)
            print(x,"+",y,"= ",end="")
            m = input()
            if m.isdigit():
                if int(m)==x+y:
                    count += 1
                    break
                else:
                    print('EEE')
            else:
                print('EEE')
            i -= 1
        if i==0:
            print(x,"+",y,"=",x+y)
    print('Score:',count)
def get_level():
    x= input("Level: ")
    if x.isdigit():
        if 1<=int(x) and int(x)<=3:
                return int(x)
        else:
            get_level()
    else:
        get_level()
def generate_integer(lvl):
    if lvl == 1:
        return random.randint(0,9)
    elif lvl == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)
if __name__=="__main__":
    main()
