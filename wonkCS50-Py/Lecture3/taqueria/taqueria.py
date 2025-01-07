menu = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

total_cost = 0

while True:
    try:
        user_input = input("Please enter an item: ").lower()
        if user_input in menu:
            total_cost += menu[user_input]

        print("Current total: ${:.2f}".format(total_cost))

    except EOFError:
        print("\nExiting...")
        break
