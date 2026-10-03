from menu import display_menu
from order import take_order, calculate_order
from receipt import print_receipt


def main():

    menu = {
        "Burger": 80,
        "Chicken": 120,
        "Spaghetti": 100,
        "French Fries": 60,
        "Softdrink": 40
    }

    display_menu(menu)

    want_order = input("\nDo you want to order? (yes/no): ")

    if want_order.lower() == "yes":

        orders = take_order(menu)

        if len(orders) > 0:
            receipt, total = calculate_order(menu, orders)
            print_receipt(receipt, total)

        else:
            print("No order was made.")

    else:
        print("Thank you! Goodbye.")


main()