import random
level = 0
guess = 0
r = 0

while level == 0 and level < 11:
    inp = int(input("Level: "))
    if type(inp) == int:
        level = inp
    else:
        pass

def gen_num(r, level):
    r = random.randint(1, level)
    return r

r = gen_num(r, level)

while guess != r:
    guess = int(input("Guess: "))
    if guess > r:
        print("Too large!")
    elif guess < r:
        print("Too small!")
    elif guess == r:\
        print("Just right!")
    elif type(guess) == int:
        continue
    else:
        pass
