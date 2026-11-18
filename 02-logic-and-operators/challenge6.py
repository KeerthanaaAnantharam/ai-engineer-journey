# valid the quality and correctness of passwords
# 1. must not be empty
# 2. must be atleast 8 characters long
# 3. must contain atleast 1 upper case 
# 4. must contain atleast 1 lower case
# 5. must not be the same as the email
# 6. must not contain any spaces
# 7. must start and end with a letter or digit
email = "Abc@gmail.com"
password = "aaaa"
valid = True
#clean
password = password.strip()

# must not be empty
if(password == ""):
    print("password cannot be empty")
    valid = False
# must be atleast 8 characters long
if(len(password) < 8):
    print("Password must be atleast 8 characters long")
    valid = False
# must contain atleast 1 upper case 
if(password == password.lower()):
    print("Password must contain atleast one upper case letter")
    valid = False
# must contain atleast 1 lower case
if(password == password.upper()):
    print("Password must contain atleast one lower case letter")
    valid = False
# must not be the same as the email
if(password == email):
    print("Password must not be the same as Email")
    valid = False
# must not contain any spaces
if(" " in password):
    print("Password must not contain spaces")
    valid = False
# must start and end with a letter or digit
if not (password[0].isalnum() and password[-1].isalnum()):
    print("Password must start and end with letter or digit")
    valid = False
if valid:
    print("Password is valid")

