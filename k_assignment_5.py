class Product:
    def __init__(self):
        self.inventory = [] #creating list to store products
        self.category = {} #create dictionary to categorize products

    def check_if_expired(self, curr_date):
        return [product for product in self.inventory if self.is_expired(product['Expiry date'], curr_date)]

    def is_expired(self, expiry_date, curr_date):
        exp_day, exp_month, exp_year = expiry_date.split('-') #splitting to get day, month and year from date and compare current date with expiry date
        curr_day, curr_month, curr_year = curr_date.split('-')

        exp_day = int(exp_day) #typecasting to integer type
        exp_month = int(exp_month)
        exp_year = int(exp_year)
        curr_day = int(curr_day)
        curr_month = int(curr_month)
        curr_year = int(curr_year)

        if exp_year < curr_year or (exp_year == curr_year and exp_month < curr_month) or (exp_year == curr_year and exp_month == curr_month and exp_day < curr_day):
            return True
        return False

    def add_product(self, name, category, price, quantity, exp_date): #function to add product to list
        for product in self.inventory:
            if product['Name'] == name: #updates quantity of product if product already present in list
                print(f'{name} already present in inventory. Update quantity? (1 to update, 2 to add as a new product)')
                choice = int(input('Enter choice: '))
                if choice == 1:
                    product['Quantity'] += quantity
                elif choice == 2:
                    self.inventory.append({'Name': name, 'Category': category, 'Price': price, 'Quantity': quantity, 'Expiry date': exp_date})
                self.categorize_product()
                return
        else:
            self.inventory.append({'Name': name, 'Category': category, 'Price': price, 'Quantity': quantity, 'Expiry date': exp_date})
            print(f'{name} added to inventory')
            self.categorize_product()

    def remove_product(self, name): #function to remove product from list
        removed = False
        for product in self.inventory:
            if product['Name'] == name:
                self.inventory.remove(product)
                removed = True
                print(f'{name} removed from inventory')
                break
        if not removed:
            print(f'{name} is not present in the inventory. Please check the spelling or enter another product to remove.')

    def search(self, s): #function to search for a product in list based on search term given by user
        s = s.lower() #converting to lowercase for comparison
        matches = [product for product in self.inventory if s in product['Name'].lower() or s in product['Category'].lower()] #comparing search term with name and category(all in lowercase)
        if matches:
            print('Match found:')
            for product in matches:
                print(f'Name: {product['Name']}, Category: {product['Category']}, Price: {product['Price']}, Quantity: {product['Quantity']}, Expiry Date: {product['Expiry date']}')
        else:
            print('No such item present in inventory.')

    def list_product(self): #function to display products in list
        if self.inventory == []:
            print('Inventory is empty.')
        else:
            for product in self.inventory:
                print(f'Name: {product['Name']}, Category: {product['Category']}, Price: {product['Price']}, Quantity: {product['Quantity']}, Expiry Date: {product['Expiry date']}')

    def categorize_product(self): #function to categorize products in list into different categories
        self.category = {}
        for product in self.inventory:
            cat = product['Category']
            if cat not in self.category:
               self.category[cat] = []
            self.category[cat].append(product) 

    def print_by_category(self, cat_name): #function to print items of the same category
        if cat_name in self.category:
            print(f'Products in {cat_name} category:')
            for product in self.category[cat_name]:
                print(f'Name: {product['Name']}, Category: {product['Category']}, Price: {product['Price']}, Quantity: {product['Quantity']}, Expiry Date: {product['Expiry date']}')
        else:
            print('No products in this category.')

    def check_expired_product(self, curr_date): #function to check which products are expired an remove them from list
        expired_products = self.check_if_expired(curr_date)
        if expired_products:
            print('Expired items present in inventory and removed:')
            for product in expired_products:
                print(product)
                self.inventory.remove(product)
        else:
            print('No expired products in the inventory.')

    def save_inventory(self, file): #function to save inventory to a file specified
        try:
            with open(file, 'a+') as f:
                for product in self.inventory:
                    f.write(f'{product['Name']}, {product['Category']}, {product['Price']}, {product['Quantity']}, {product['Expiry date']}\n')
            print('Saved')
        except IOError as e:
            print('Error while trying to save',e)

    def load_inventory(self, file): #function to load the list from the file to the inventory
        try:
            with open(file, 'r') as f:
                self.inventory = []
                for line in f:
                    name, category, price, quantity, expirydate = line.split(', ')
                    self.inventory.append({'Name': name, 'Category': category, 'Price': price, 'Quantity': quantity, 'Expiry date': expirydate})
                self.categorize_product()
                print('Inventory loaded successfully.')
        except IOError as e:
            print('Error while loading', e)

p = Product() 
p.load_inventory('sample.txt')

choice = 0
while choice != 8:
    print('1. Add product \n2. Remove product \n3. Search product \n4. List products \n5. Print products by category \n6. Check and remove expired products \n7. Save inventory \n8. Exit\n')

    choice = int(input('Enter choice (1-9): '))

    if choice == 1:
        name = input('Product name: ')
        category = input('Category: ')
        price = int(input('Price: '))
        quantity = int(input('Quantity: '))
        exp_date = input('Expiry date (DD-MM-YYYY): ')
        p.add_product(name, category, price, quantity, exp_date)

    elif choice == 2:
        name = input('Enter name of product to remove from inventory: ')
        p.remove_product(name)

    elif choice == 3:
        s = input('Enter name or category to search: ')
        p.search(s)

    elif choice == 4:
        p.list_product()

    elif choice == 5:
        cat = input('Enter category to print: ')
        p.print_by_category(cat)

    elif choice == 6:
        date = input('Enter todays date (DD-MM-YYYY): ')
        p.check_expired_product(date)

    elif choice == 7:
        p.save_inventory('sample.txt')

    elif choice == 8:
        p.save_inventory('sample.txt')
        print('Exiting...')

    else:
        print('Invalid choice. Please choose from 1 to 8.')
