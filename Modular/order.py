def take_order(menu):
    orders = []

    while True:
        item_name = input("\nEnter menu item: ")

        if item_name in menu:
            quantity = int(input("Enter quantity: "))

            orders.append([item_name, quantity])
            print("Item added to your order.")

        else:
            print("Item not found in the menu.")

        another = input("Do you want to order another item? (yes/no): ")

        if another.lower() == "no":
            break

    return orders


def calculate_order(menu, orders):
    total = 0
    receipt = []

    for order in orders:
        item_name = order[0]
        quantity = order[1]
        price = menu[item_name]
        item_total = price * quantity

        receipt.append([item_name, quantity, price, item_total])
        total += item_total

    return receipt, total