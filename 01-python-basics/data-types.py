#python automatically detects the data type of a variable based on the value assigned to it.
a=10
b='hi'

print(type(a)) #returns <class 'int'> because a is an integer
print(type(b)) #returns <class 'str'> because b is a string

a=10
print(a.bit_length()) #returns 4 because 10 in binary is 1010 which is 4 bits long

text="Hello Python"
print(text.upper()) #returns HELLO PYTHON because upper() converts all characters to uppercase


