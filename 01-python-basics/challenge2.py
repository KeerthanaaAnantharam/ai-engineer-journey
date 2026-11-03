#print the following statements using variables
#add a variable to make it dynamic
#info@keetsjourney.com
#support@keetsjourney.com
#www.keetsjourney.com

name = "keetsjourney"
print("info@", name, ".com")
print("support@", name, ".com")
print("www.", name, ".com")

#we can also use f-strings to make it more readable and remove the extra spaces
#The f before the quotes tells Python: “anything inside { } is a variable, so swap in its value.” 
# It’s like a fill-in-the-blank template.
print(f"info@{name}.com")
print(f"support@{name}.com")
print(f"www.{name}.com")

#we can also use the sep parameter in the print function to remove the extra spaces
print("info@", name, ".com", sep="")
print("support@", name, ".com", sep="")
print("www.", name, ".com", sep="")