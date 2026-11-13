#types
import math

x=5
print(type(x))

y=5.7
print(type(y))

z=2+3j
print(type(z))

a ="24"
a = int(a)
print(type(a))

b = 5
print(float(b)) #returns 5.0 because float() converts the integer to a float

#rounding
price = 35.85995695
print(round(price))
print(round(price, 2)) #returns 35.86 because round() rounds the float to 2 decimal places

#math functions
x = 5.6
print(math.ceil(x))  # returns 6 because ceil() rounds the float up to the nearest integer
print(math.floor(x)) # returns 5 because floor() rounds the float down to the nearest integer
print(math.sqrt(16)) # returns 4.0 because sqrt() calculates the square root of the number
    
#validations
x1 = 4.5
print(isinstance(x1, (int, float)))  # returns True because isinstance() checks if the variable is of a specific type

a1 = 5.3
print(a1.is_integer()) #returns False because is_integer() checks if the float is an integer
b1 = 5.0
print(b1.is_integer()) #returns True because is_integer() checks if the float is an

