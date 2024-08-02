with open('sample.txt', 'r') as f:
    for line in f:
        name, category, price, quantity, expdate = line.split(', ')
        print(name)
        print(category)
        print(price)
        print(quantity)
        print(expdate)