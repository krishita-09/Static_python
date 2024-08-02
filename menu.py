from exceptions import InvalidMenuItemError

class MenuItem: 
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Menu:
    def __init__(self):
        self.menu_items = []    #creating a list

    def read_menu_from_file(self, filename): #function to read from file specified
        try:
            with open(filename, "r+") as file:
                for line in file:
                    name, price, quantity = line.strip().split(',')
                    self.menu_items.append(MenuItem(name, float(price), int(quantity)))
            print("Menu loaded from file.")
        except FileNotFoundError:
            print("File not found.")

    def add_item(self, name, price, quantity): #function to add items to menu
        for item in self.menu_items:
            if item.name == name:
                print(f"'{name}' already exists in the menu.")
                return
        
        new_item = MenuItem(name, price, quantity)
        self.menu_items.append(new_item)
        print(f"Item '{name}' added to the menu.")

    def update_item(self, name, price, quantity):   #function to update quantity and/or price fo item specified
        match = False
        for item in self.menu_items:
            if item.name == name:
                item.price = price
                item.quantity = quantity
                print(f"Item '{name}' updated.")
                match = True
                break
        if match == False:
            raise InvalidMenuItemError("Item not found in the menu.")

    def delete_item(self, name):    #function to delete from menu
        match = False
        for item in self.menu_items:
            if item.name == name:
                self.menu_items.remove(item)
                print(f"Item '{name}' deleted from the menu.")
                match = True
                break
        if match == False:
            raise InvalidMenuItemError(f"Item '{name}' not found in the menu.")

    def display_menu(self):
        if not self.menu_items:
            print("Menu is empty.")
        else:
            print("Menu:")
            for item in self.menu_items:
                print(f"Name: {item.name}, Price: {item.price}, Quantity: {item.quantity}")

    def write_menu_to_file(self, filename): #function to append to menu
        try:
            with open(filename, "a+") as file:
                for item in self.menu_items:
                    file.write(f"{item.name},{item.price},{item.quantity}\n")
            print("Menu saved to file.")
        except Exception as e:
            print(f"Problem while trying to save menu to file, {e}")
