def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

result = None
ch1 = 0
ch2 = 0


while ch1 != 4:
    ch1 = int(input("Select: \n 1. Choose operation \n 2. Input value \n 3. Display result \n 4. Exit \n "))

    if ch1 == 1:
        ch2 = int(input("Select: \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n"))
    elif ch1 == 2:
        if ch2 in (1, 2, 3, 4):
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            
            if ch2 == 1:
                result = add(a,b)
            elif ch2 == 2:
                result = sub(a,b)
            elif ch2 == 3:
                result = mul(a,b)
            elif ch2 == 4:
                if b == 0:
                    print("Number cannot be divided by 0.")
                else:
                    result = div(a,b)
        else:
            print("Invalid Choice")

    elif ch1 == 3:
        if result is not None:
            print(result)
        else:
            print("Preform calculation.")

    elif ch1 != 4:
        print("Invalid Choice.")
    else:
        break
exit
