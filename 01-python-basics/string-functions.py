age = 24
print(str(age)) #returns '24' because str() converts the integer to a string    

password = "Python123"
print(len(password)) #returns 9 because len() returns the number of characters in the string
if(len(password) >= 8):
    print("Password is valid") #returns Password is valid because the length of the password is greater than or equal to 8  
    
text ="""Python is easy to learn.
Python is powerful.
Python is fun."""

print(text.count("Python")) #returns 3 because count() counts the number of occurrences of the substring "Python" in the string 

date = "2024-06-15"
print(date.replace("-", "/")) #returns 2024/06/15 because replace() replaces all occurrences of "-" with "/" in the string

price = "$1,299.99"
print(price.replace("$", "").replace(",", "")) #returns 1299.99 because replace() removes the "$" and "," from the string

