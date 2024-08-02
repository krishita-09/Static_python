from exceptions import InvalidMenuItemError, InsufficientQuantityError

class Order:
    def __init__(self, menu):
        self.menu = menu
        self.order_items = []   #creating list to store data

    def write_orders_to_file(self, filename):   #function to append order to the file specified
        try:
            with open(filename, "a+") as file:
                for item in self.order_items:
                    file.write(f"{item['name']},{item['price']},{item['quantity']}\n")
            print("Orders saved to file.")
        except FileNotFoundError:
            print("File not found.")

    def read_orders_from_file(self, filename):  #function to read order from file specified
        try:
            self.past_orders = []   #list to store previous order to show the current order made
            with open(filename, 'r+') as file:
                for line in file:
                    name, price, quantity = line.strip().split(',') #use strip to remove spacing and split to divide the string
                    self.past_orders.append({'Name': name,'Price': float(price),'Quantity': int(quantity)})
            print("Order loaded from file.")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")

    def add_item(self, name, quantity): #function to add item to order and decrease it's quantity 
        match = False
        
        for item in self.menu.menu_items:
            if item.name == name:
                if item.quantity >= quantity:
                    self.order_items.append({'name': name,'price': item.price,'quantity': quantity})
                    print("Item added to the order")
                    item.quantity -= quantity
                    match = True
                    break
                else:
                    raise InsufficientQuantityError(name, item.quantity)    #raises custom exception if quantity ordered by user is more than quantity present
        
        if match == False:
            raise InvalidMenuItemError(f"Item not found on the menu.")  
    def take_order(self):
        ordering = True
        while ordering:
            try:
                name = input("Name: ").title()
                quantity = int(input("Quantity: "))
                
                self.add_item(name, quantity)
                self.display_current_order()  # Display current order after adding each item

                add_another = input("Add another item? (y/n): ").lower() #used to take one more item until user types n 
                if add_another != 'y':
                    ordering = False

            except ValueError:
                print("Invalid value")
            
            except InsufficientQuantityError as e:
                print(e)

            except InvalidMenuItemError as e:
                print(e)
                break

    def display_order(self):    #function to display order
        if not self.order_items:
            print("No items in order.")
        else:
            print("Current Order:")
            for item in self.order_items:
                print(f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")

    def calculate_total(self):#function to calculate bill
         bill = 0.0
         for item in self.order_items:
            price = item['price'] * item['quantity']
            bill += price
            return bill


    def receipt(self):  #function to create a bill with items ordered, quantity and total
        total_bill = self.calculate_total()
        for item in self.order_items:
            print(f"{item['name']} : {item['price']} * {item['quantity']}")
        print(f"Amount: {total_bill:.2f}")

        self.write_orders_to_file("orders.txt")

        for order_item in self.order_items:
            for menu_item in self.menu.menu_items:
                if menu_item.name == order_item["name"]:
                    menu_item.quantity -= order_item["quantity"]
                    break

        self.order_items = []
