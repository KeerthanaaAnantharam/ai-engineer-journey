#convert the messy phone number into a cleaner format with only digits using string functions

phone_number = "+49 (176) 123-4567"
print(phone_number.replace("+", "00").replace("(", "").replace(")", "").replace("-", "").replace(" ", "")) #returns 491761234567 because replace() removes all non-digit characters from the string