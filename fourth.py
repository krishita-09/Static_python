'''
list = [1,2,3,4,5,6,7,8]
print(list[2:5])

tuple = 1,2,3,4,5,6,7,8,9,0
print(tuple[3:])

list = [3,2,2,3]
for i in list:
    # print(i)
    pass 

list = [x for x in range (1,11) if x!=7]
# print(list)


for i in range (1,11):
    if i!=7:
        print(i)
    else:
        continue


a = 'apple'
for i in a:
    if i == 'p':
        continue
    else:
        print(i)


def sample():
    pass 
 sample()


list = [1,2,3,4,6,7,8,9,11]
for i in range(1,11):
    if i in list:
        pass
    else:
        list.append(i)
#list.sort()
print(list)


def search(list,name,val):
    val1 = val
    if list[val] == name:
        print('found at',val)
    else:
        val1 += 1
        search(list,name,val1)

list = ['swara','sam','krish','stuti']
search(list,'sam',1)

class Classroom:
    student = ['a','b']
    teacher = 'p'

obj = Classroom
print(obj.teacher)

def timepass():
    print("Kuch toh sikhaya par maine dhyaan nahi diya")

timepass()

class Student:
    Name = 'Krish'
    r_no = 10
    rank = 100
    def all(self):
        print(f"{self.Name} is roll no {self.r_no}")


class Bird:
    def _init_(self):
        print("Bird is ready")

class Penguin(Bird):
    def _init_(self):
        super()._init_()
        print("Penguin is ready")

peggy = Penguin()

num = [3,2,1,2,3,5,7,9,3,2,6,3,7,3,2,6,4,3,6,8,6,8,9,0,4,3,7,5,8,5,8,3,2,3]
val = 1
list = [num[i] for i in range(len(num)) if num[i] != val]
print(list)
'''
