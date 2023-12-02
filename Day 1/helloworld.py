# 1. Check the python version you are using
import sys
print(sys.version)

# 2. Open the python interactive shell and do the following operations. The operands are 3 and 4.

print(3+4) # addition
print(3-4) # subtraction
print(3*4) # multiplication
print(3/4) # division
print(3**4) # exponentiation
print(3 % 4) # modulos
print(3//4) # floor division

# 3. Write strings on the python interactive shell. The strings are the following:
print('Abdulrahman Ahmed')
print('Oriabure')
print('Nigeria')
print('I am enjoying 30 days of python')

# 4. Check the data types of the following data:
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('Abdulrahman'))
print(type('Oriabure'))
print(type('Nigeria'))


# Level 3 exercise
# Python Data types
# Number : Integer, Float, Complex
a = 1 # Integer
print(type(a))
b = 9.586 # Float
print(type(b))
c = 5 + 3j # Complex
print(type(c))
# String : 
d = 'Abdulrahman' # String
print(type(d))
# Boolean :
e = True # Boolean
print(type(e))
# List:
f = ['Haleemah',4,8.5,True,False,['Chicken']] #Square brackets
print(type(f))
# Tuple:
g = ("red","green") #Round brackets
print(type(g))
# Set :
h = {2,4,6,8} # set - Curly brackets
print(type(h))
# Dictionary: 
i = {'goat':7,'dog':8,'Chicken':9}
print(type(i))

#Euclidian distance
# import math module
import math
print(math.dist([4,6],[20,4]))