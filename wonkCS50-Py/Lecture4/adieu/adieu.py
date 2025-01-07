import inflect
i = inflect.engine()
names = []

while True:
    try:
        inp = input("Name: ")
        names.append(inp)
    except KeyboardInterrupt:
        break
    except EOFError:
        break

print(f'Adieu, adieu, to {i.join(names)}')
