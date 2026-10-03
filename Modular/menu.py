def display_menu(menu):
    print("\n===== FAST FOOD MENU =====")

    number = 1
    for item, price in menu.items():
        print(number, ".", item, "- P", price)
        number += 1