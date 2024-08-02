def c_to_f(c):
    f = c*(9/5)+32
    return f

def f_to_c(f):
    c = (f-32)*(5/9)
    return c

ch1 = 0
n = None  
t = None 

while ch1 != 4:
    ch1 = int(input('Select: \n 1. Enter Input \n 2. Choose conversion \n 3. Display result \n 4. Exit \n')) 
    if ch1 == 1:
        n=int(input('Enter value: '))
    elif ch1 == 2:  
        if n is None:
            print('Enter an input')
        else:
            ch2 = int(input('Select: \n 1. Celsius to Farenheit \n 2. Farenheit to Celsius \n'))
            if ch2 == 1:
                t = c_to_f(n)
            elif ch2 == 2:
                t = f_to_c(n)
            else:
                print("Invalid Choice")
    elif ch1 == 3:
        if t is None:
            print('Perform conversion')
        else:
            print(t)
    elif ch1 != 4:
        print('Invalid Choice')
    else:
        break
exit

