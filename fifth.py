'''
class new:
    def __init__(self):
        print("This is a default constructor")
    
a = new()


#magic function
#dender

class new2:
    def __init__(self,n,r):
        self.name = n 
        self.r_no = r
    def call(self):
        print(f"{self.name}'s roll no is {self.r_no}")

b = new2('S' , 20)
b.call()
b.name = 'P'
b.r_no = 10
b.call()

class new2:
    def __init__(self,n,r):
        self.name = n
        self.r_no = r
    def call(self):
        print(f"{self.name}'s roll no is {self.r_no}")

b = new2('s',20)
b.call()
b.name = "p"
b.r_no= 20
b.call()


class Base:
    def __init__(self):
        self._a = 2 # single underscore ->protected double underscore ->private

class Derived(Base):
    def __init__(self):

        Base.__init__(self)
        print("Calling protected member of base class: ",self._a)

        self._a = 3
        print("Calling modified protected member of class : ",self._a)

obj1 = Derived()
#obj2 = Base()

class base:
    def __init__(self):
        self.__a= 2 

class derived(base):
    def __init__(self):
        base.__init__(self)
        print("calling protected",self._base__a) #name mangling :- can inherit private members 

        self._a = 4
        print("calling modified protected",self._a)
obj1 = derived()
obj =  base()       


class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

class Car(Vehicle):
    def move(self):
        print("Move!")

class Boat(Vehicle):
    def move(self):
        print("Sail!")
    
class Plane(Vehicle):
    def move(self):
        print("Fly")

car1 = Car("Porche", "2014")
boat1 = Boat("Speed", "2020")
plane1= Plane("Fighter", "2022")

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.year)
    x.move()


class fruits:
    def __init__(self,taste,price):
        self.taste = taste
        self.price = price
class mango(fruits):
    def colour(self):
        print("narangi")

class orange(fruits):
    def colour(self):
        print("orange")

class grape(fruits):
    def colour(self):
        print("dark purple")

m1 = mango("sweet", "1500")
o1 = orange("khatta-mitha", "600")
g1 = grape("sweet", "500")
for x in (m1, o1, g1):
    print(x.taste)
    print(x.price)
    x.colour()      


class student:
    def __init__(self, name, id):
        self.name = name
        self.id = id 

class branch(student):
    def __init__(self, name, id, b):
        super().__init__(name, id)
        self.b = b


i = branch('krish', 10, 'CO')
print(i.name)
print(i.id)
print(i.b)
 


class mother:
    def __init__(self, mname) -> None:
        self.name = mname

class father:
    def __init__(self, fname) -> None:
        self.name = fname

class surname:
    def __init__(self, sname) -> None:
        self.name = sname

class child(mother, father, surname):
    def __init__(self, name, fname, sname, mname) -> None:
        self.name = name
        mother.__init__(self, mname)
        father.__init__(self, fname)
        surname.__init__(self, sname)
        print(name, mname, fname, sname)

c = child('a', 'b', 'c', 'd')


#yeh feature sirf ache website offer karte hai
def dec(func):
    def process():
        print("Welcome")
        func()
        print("Goodbye")
    return process

@dec 
def yes():
    print("krish")

yes()

file = open("demo.txt","w")
file.write("hello this is my file")
file.close()

with open("C:\\Users\\KRISHUSEEMI\\Documents\\Java\\jdk-1.8\\bin\\swara.txt","w") as file:
    file.write("hello!")


with open("example.txt","r") as file:
    print("\nReading line by line: ")
    for line in file:
        print(line.strip())

with open("example.txt","a") as file:
    file.write("\nappended line") 

with open("example.txt","r") as file:
    file.seek(3)
    print("\nReading from 0th character onwards: ")
    rem_content = file.read()
    print("Remaining content")


with open("example.txt","r+") as file:
    file.write("hgcvfghjtdsdcvb")
    file.seek(0)
    con = file.read()

with open("example.txt","a+") as file:
    file.write("\ni worked my whole life ")
    file.seek(0)
    con=file.read()
    print(con)

'''