'''
tuple=1,2,3
print(type(tuple))
list=list(tuple)
print(type(tuple[1]))


dict = {'name':'abc','rollno':1}
print(dict)
print(type(dict))

dict1 = {
    'key':[1,2,3,4],
    'key1':[5,6,7,8]
}
print(dict1)
print(type(dict1))

print(type(dict1['key']))
list = dict1['key'].extend(dict1['key1'])
print(list)

x=8
for i in range(1,11):
    print({x:x**3})
    x+=1

sqr={x:x**3 for x in range(1,11) if x!=7}
print(sqr.items())

list = [x for x in range(2,9) if x!=5]
print(list)

y=14
list = [x*y for x in range(101,122)]
print(list)

x=2
list = [x for x in range(2,30,2)]
print(list)

user = int(input('Message '))5
print(user)

list = []
n = int(input('Enter length '))
for i in range(n):
    user = int(input(f'{i+1} Value '))
    list.append(user)
print(list)

def sample(x,y):
    c=x*y
    return c
p = sample(4,4)
print(p)    

def sample():
    s = 0
    for i in range(5):
        a = int(input())
        s += a
    return s
sum = sample()
print(sum)

print(int(abs(-192928.99999)))


def sample(name,roll_no):
    print(f'{name} is roll_no {roll_no}')

p = sample(roll_no=20,name='Krish')
print(p)  


def avg_age():
    sum = 0
    for i in range(10):
        a = int(input("Enter age "))
        sum += a
    avg = sum/10
    return avg
average_age = avg_age()
print(average_age)

def a():
    list = []
    n = int(input('Enter no. of students: '))
    for i in range(n):
        user = int(input(f'{i+1} Age: '))
        list.append(user)
    s = sum(list)
    avg = s/n
    return avg
avg_age = a()
print(avg_age)

def age(*b):
    print(b)
    print(type(b))

age(1,2,3,4)


print('kuch toh')

'''
def my_func(**kid):
    print(" come a little closer cause you looking thirsty imma make it better sip it like a slurpee snow cone chilly get it free like willy in the jeans like billy you be popping like a wheelie even in the sun you know i keep it icy you could take a lick but it's to cold to bite me brr brr frozen you the one been chosen play the part like moses keep it fresh like roses you look so good you look so sweet looking good enough to eat diamond on my wrist so he call me icecream catch me in the fridge where ice be coldest with the kiss so he call me icecream   ")

a=my_func(name="krishi")
