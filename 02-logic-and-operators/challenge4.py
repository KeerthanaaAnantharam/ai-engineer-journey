#check if a user's name is not empty and the age is greater than or equal to 18
#check if the password is 8 characters long and does not contain spaces
#check if the user's email is not empty, contains '@' and ends with '.com'
#check if a username is string, is not None and is longer than 5 characters
#check if the user is either an admin or a moderator and either they are not banned or they have verified email.

#1 solution
username = "John"
age = 20
print((username is not None and username != "") and age >=18)

#2 solution
password = "test1234"
print(len(password) == 8 and " " not in password)

#3 solution
email = "test@yahoo.com"
print((email is not None and email != " ") and "@" in email and email.endswith(".com"))

#4 solution
username = "Abraham Lincoln"
print(isinstance(username, str) and username is not None and len(username) >= 5)

#5 solution
user ="admin"
is_banned = False
is_email_verified = True

user_types = ['admin', 'moderator']
print(user in user_types and is_banned == False and is_email_verified == True)
