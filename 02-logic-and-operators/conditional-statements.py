#if
score = 100
if(score > 90):
    print("First Class")

#else
score = 45
if(score > 90):
    print("First Class")
else:
    print("Average")
    
#elif (branching)
score = 80
if(score >= 90):
    print("Grade A")
elif(score >= 80):
    print("Grade B")
elif(score >= 70):
    print("Grade C")
elif(score >= 60):
    print("Grade D")
else:
    print("Grade F")
    
#nested if
score = 88
project_submitted = False

if(score > 80 and project_submitted):
    print("Grade A+")
elif (score > 80 or project_submitted):
    print("Grade A")

