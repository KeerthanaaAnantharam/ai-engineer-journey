#turn the messy string into a single clean summary with name , role and age
# "968-Maria, ( D@t@ Engineer  );; 27y  "
# name: maria | role: Data Engineer | age: 27
messy_string = "968-Maria, ( D@t@ Engineer  );; 27y  "
# Step 1: Remove leading and trailing spaces
clean_string = messy_string.strip()
print(clean_string)  # Output: 968-Maria, ( D@t@ Engineer  );; 27y
# Step 2: extract the name
name = clean_string[4:9].strip().lower()  # Extracts maria and converts it to lowercase
print(name)  # Output: maria
# Step 3: extract the role
role = clean_string[13:26].strip().replace("@", "a")  # Extracts D@t@ Engineer, removes leading/trailing spaces, and replaces "@" with "a"
print(role)  # Output: Data Engineer
# Step 4: extract the age
age = clean_string[32:34]  # Extracts 27y and removes leading/trailing spaces
print(age)  # Output: 27
# Step 5: Create the clean summary
clean_summary = f"name: {name} | role: {role} | age: {age}"
print(clean_summary)  # Output: name: maria | role: Data Engineer | age:

