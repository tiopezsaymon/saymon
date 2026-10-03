from fastfood import FastFoodSystem

def main():

    system = FastFoodSystem()

    system.display_menu()

    want_order = input("\nDo you want to order? (yes/no): ")

    if want_order.lower() == "yes":

        system.take_order()

        if len(system.orders) > 0:
            receipt, total = system.calculate_order()
            system.print_receipt(receipt, total)
        else:
            print("No order was made.")

    else:
        print("Thank you! Goodbye.")


main()