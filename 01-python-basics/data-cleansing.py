#remove spaces
text = " Hello"
print(text.lstrip()) #returns 'Hello' because lstrip() removes leading spaces from the string

text = "Hello "
print(text.rstrip()) #returns 'Hello' because rstrip() removes trailing spaces from the string

text = " Hello "
print(text.strip()) #returns 'Hello' because strip() removes leading and trailing spaces from the string

text = "###Hello###"
print(text.strip("#")) #returns 'Hello' because strip() removes leading and trailing "#" characters from the string

text = "  Engineering"
print(len(text()))
print(len(text.strip())) #returns 11 because strip() removes leading spaces and len() returns the number of characters in the string

no_of_spaces = len(text) - len(text.strip())
is_clean = len(text.strip()) == len(text.strip())
print("Number of spaces removed:", no_of_spaces) #returns Number of spaces removed: 2 because len() returns the number of characters in the string before and after stripping spaces
print("Is the text clean?", is_clean) #returns Is the text clean? True because len() returns the number of characters in the string after stripping spaces and compares it with the original length

#case conversion
text = "python"
print(text.upper()) #returns 'PYTHON' because upper() converts all characters in the string to uppercase

text = "PYTHON"
print(text.lower()) #returns 'python' because lower() converts all characters in the string to

search = "Email"
data = "email"

print(search == data) #returns False because the comparison is case-sensitive and "Email" is not equal to "email"

search = "Email "
data = " email"

print(search.strip().lower() == data.strip().lower()) #returns True because strip() removes leading and trailing spaces and lower() converts both strings to lowercase before comparison

