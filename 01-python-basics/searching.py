#data search
phone = "+49 123 456 789"
print(phone.startswith("+49")) #True

email = "keets@gmail.com"
print(email.endswith("@gmail.com")) #True
print("@" in email) #True

file = "data.csv"
print(file.endswith(".csv")) #True

#print phone numbers without country code
phone1 = "+49-123-456-789"
phone2 = "49-567-234-567"
print(phone1[4:])
print(phone2[3:])

#using find() to locate the position of a substring
print(phone1[phone1.find("-")+1:])
print(phone2[phone2.find("-")+1:])



