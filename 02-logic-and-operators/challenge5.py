#valdate the quality and correctness of email
# 1. must not be empty
# 2. must contain '.' and '@'
# 3. must contain exactly one '@'
# 4. must end with .com or .net or .org
# 5. must not be longer than 254 characters
# 6. must start and end with a letter or digit

email = "  "
valid = True
#clean the data 
# email must not be empty
email = email.strip()
if(email == ""):
    print("Email cannot be empty")
    valid = False
# must contain '.' and '@'
if not('.' in email and '@' in email):
    print("Email must contain a dot and @")
    valid = False
#  must contain exactly one '@'
if email.count('@') != 1:
    print("Email must contain exactly only one @")
    valid = False
# must end with .com or .net or .org
if not email.endswith(('.com', '.net', '.org')):
    print("Email must end with .com or .net or .org")
    valid = False
# must not be longer than 254 characters
if len(email) > 254:
    print("Email must not be longer than 254 characters")
    valid = False
# must start and end with a letter or digit
if not (email[0].isalnum() and email[-1].isalnum()):
    print("Email must start with letter or digit")
    valid = False
    
if valid:
    print("Valid Email")
    
