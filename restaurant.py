import menu     #importing modules to use classes and functions presnt in module
import order
from exceptions import InvalidMenuItemError,InsufficientQuantityError

menu_m = menu.Menu()    #creating instances of classes
order_o = order.Order(menu_m)

menu_m.read_menu_from_file('menu.txt')  #to load previously stored data  
order_o.read_orders_from_file('orders.txt')

choice = 0
while choice != 8:
    print("\nRestaurant Management System \n1. Add item to menu \n2. Update item in menu \n3. Delete item from menu \n4. Display menu \n5. New order \n6. View order \n7. Generate receipt \n8. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Name: ").title    #taking user input in title case 
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        menu_m.add_item(name, price, quantity)
        menu_m.write_menu_to_file('menu.txt')

    elif choice == '2':
        name = input("Enter item name: ").title()
        price = float(input("Updated price: "))
        quantity = int(input("Updated quantity: "))
        try:
            menu_m.update_item(name, price, quantity)
            menu_m.write_menu_to_file('menu.txt')
        except InvalidMenuItemError as e:   #throws a custom exception when the item entered by user is not present in list
            print(e)

    elif choice == '3':
        name = input("Enter item name to delete: ").title()
        try:
            menu_m.delete_item(name)
            menu_m.write_menu_to_file('menu.txt')
        except InvalidMenuItemError as e:
            print(e)

    elif choice == '4':
        menu_m.display_menu()

    elif choice == '5':
        order_o.take_order()
        order_o.receipt()
        order_o.write_orders_to_file('orders.txt')
        order_o.display_order()

    elif choice == '6':
        order_o.display_order()

    elif choice == '7':
        order_o.receipt()
        order_o.write_orders_to_file('orders.txt')

    elif choice == '8':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter a number between 1-8.")
