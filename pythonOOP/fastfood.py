class FastFoodSystem:

    def __init__(self):
        self.menu = {
            "Burger": 80,
            "Chicken": 120,
            "Spaghetti": 100,
            "French Fries": 60,
            "Softdrink": 40
        }
        self.orders = []

    def display_menu(self):
        print("\n===== FAST FOOD MENU =====")

        number = 1
        for item, price in self.menu.items():
            print(number, ".", item, "- P", price)
            number += 1

    def take_order(self):
        while True:
            item_name = input("\nEnter menu item: ")

            if item_name in self.menu:
                quantity = int(input("Enter quantity: "))
                self.orders.append([item_name, quantity])
                print("Item added to your order.")
            else:
                print("Item not found in the menu.")

            another = input("Do you want to order another item? (yes/no): ")

            if another.lower() == "no":
                break

    def calculate_order(self):
        total = 0
        receipt = []

        for item_name, quantity in self.orders:
            price = self.menu[item_name]
            item_total = price * quantity

            receipt.append([item_name, quantity, price, item_total])
            total += item_total

        return receipt, total

    def print_receipt(self, receipt, total):
        print("\n========== RECEIPT ==========")
        print("Item\t\tQty\tPrice\tTotal")

        for item in receipt:
            print(item[0], "\t\t", item[1],
                  "\tP", item[2], "\tP", item[3])

        print("-----------------------------")
        print("TOTAL: P", total)
        print("=============================")