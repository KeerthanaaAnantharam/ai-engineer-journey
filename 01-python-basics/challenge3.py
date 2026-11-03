#create 5 variables - each with different data types
#1. your age
#2. your height in decimals
#3. your name
#4. are you a student?
#5. something with no value yet
#then print the values, data types and length of each variable (if applicable)

age = 25 # integer
height = 5.9 # float
name = "John Doe" # string
is_student = True # boolean
no_value = None # NoneType

print("Age:", age, "Type:", type(age), "Length:", len(str(age))) # Length of integer is calculated by converting it to string
print("Height:", height, "Type:", type(height), "Length:", len(str(height)))
print("Name:", name, "Type:", type(name), "Length:", len(name))
print("Is Student:", is_student, "Type:", type(is_student))
print("No Value:", no_value, "Type:", type(no_value))