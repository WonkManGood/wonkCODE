inserted = int(0)
while inserted < 50:
    print("Amount Due:", 50-inserted)
    inserted += int(input("Insert Coin: "))
else:
    print("Change Owed:", (inserted - 50))
