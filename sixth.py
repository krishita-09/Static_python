
'''
try:
    pass
except Exception as e:
    print(e)

try:
    pass
except Exception:
    print(Exception)


try:
    print(y)
except Exception as e:
    print(e)

try:
    c = 9/0
except Exception as e:
    print(e)


try:
    a = int(input('Enter: '))
    c = a + 9
    print(c)
except Exception as e:
    print(e)
#finally:   ---------------------------> finally no impact.
    print('Done')


try:
    #with open('non_existent_file.txt','r') as file:
    #    content = file.read()
    i = int("String")

except IOError as e:
    print(f"Caught an I/O error: {e}")

except ValueError as v:
    print("Value error")

finally:
    print("Done")


try:
    result = '2' + 2
except TypeError as t:
    print(f"Caught a type error: {t}")


from mod import xy
print(xy(10,20))

import math
print(math.sqrt())

'''
from package import mod1 as m
from package.pack1 import *
print(m.krishita(10,20))
print(mod2.swara(10,20))
