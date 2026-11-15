#boolean
print(True) 
print(False)
print(type(True))

# any and all
email=""
phone="89067537"
username=""
print(any([email, phone, username])) # True if any of the values is truthy
print(all([email, phone, username])) # True if all of the values are truthy

#is instance
print(isinstance(1, int)) # True

#endswith startswith
text="Hello, World!"
print(text.startswith("Hello")) # True
print(text.endswith("World!")) # True

#comparison operators
print(5 == 5) # True
print("A" == "B") # False
print("a" == "A") # False
print(5 != 5) # False

#chained comparisons
print(5 < 10 < 15) # True
print(5 > 10 > 15) # False

#logical operators
print(True and False) # False
print(True or False) # True
print(not True) # False

#execution order
x = 5
y = 8
z = 6

print(x==5 or y>5 and z<4) # True
print((x==5 or y>5) and z<4) # False

#membership operator (in)
print("a" in "python") # true 
print(3 not in [1,2,3]) # false

#identity operator (is)
x=[1,2,3]
y=[1,2,3]

print(x==y) #true
print(x is y) #false

a=10
b=10

print(a==b) #true
print(a is b) #true

