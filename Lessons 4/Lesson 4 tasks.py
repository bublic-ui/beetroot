#Task 1

print('\n')



import random

random_number = random.randint(1, 10)

user = int(input('Guess the number from 1 to 10: '))

if user == random_number:
    print("you Winner")
else:
    print(f"Sorry, {random_number}")
    
print('\n')

# Task 2


name = input("Name: ")
year = int(input("Year: "))  

print(f"Hello {name}, on your next birthday you’ll be {year + 1} years old!")


print('\n')

# Task 3


import random


input_string = input("Enter a string: ")


for _ in range(5):
    print(''.join(random.choices(input_string, k=len(input_string))))