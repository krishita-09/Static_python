'''
a=50

if a<10:
    if a==5:
        print('a is 5')
    else:
        print('a less than 10 but not 5') 

if (60>a>10):
    print('a greater than 10 less than 60')
else:
    print('blah blah blah')

a=float(input("A value"))
print(type(a))


for i in range(2,20,2):
    print(i)

   
a=['a','b','c','d','e','f','g','h','i','j']
print(a[-3])
print(len(a))
if(len(a)/2==0):
    median=len(a)/2
else:
    median=(len(a)+1)/2
n=int(median)
print(a[n-1])


list=[1,9,3,2]
sum=0
for i in range(len(list)):
    print(list[i])
    sum+=list[i]
print(sum)

i=1
while(i<5):
    print(i)
    i+=1

    
i=1
password=123
user_inp=int(input("Enter password: "))
if(password==user_inp):
    print("Unlock")
else:
    print("Error")
    while i<5:
        user_inp=int(input("Enter password: "))
        if(password==user_inp):
            print("Unlock")
            break
    else:
            print("Mar tu")
            i+=1
exit

list=[1,2,3,4]
list.append(9)
print(list)
b=list.copy()
print (b)

set={2,7,8,9}
list= list(set)
b=list.copy()
print(b)
c=list.append(5)
print(c)
d=list.clear()
print(d)
print(list)
del list
print (list)
f=list.sort
print(f)


list=[6,7,3,56,3,6,2,5,4,0]
print(list)
list.sort(reverse=True)
print(list)
list.remove(56)
print(list)
list.insert(6,59)
print(list)
list.pop(4)
print(list)
list2=[98,78,89]
list.extend(list2)
print(list)
x=list.index(3)
print(x)

list=[1,2,3,4,5,6,7,8]
x=list.index(2)
print(x)
'''
