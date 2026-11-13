#generate a random integer between 1 and 100 and check if the result is an even number

import random

random_number = random.randint(1, 100)
if random_number % 2 == 0:
    print(f"{random_number} is an even number") 
    
