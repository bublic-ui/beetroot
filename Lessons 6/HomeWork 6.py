
# Task 1

import random

number = []
i = 0


while i < 10:
    number.append(random.randint(1, 100))
    i += 1
    
max_number = number[0]
i = 1
while i < len(number):
    if number[i] > max_number:
        max_number = number[i]
    i += 1
print(number)
print(max_number)
    
# Task 2

print('\n')



import random

list1 = []
list2 = []

i = 0

while i < 10:
    list1.append(random.randint(1, 100))
    list2.append(random.randint(1, 100))
    i += 1
    
common_number = []

i = 0
while i < len(list1):
    if list1[i] in list2 and list1[i] not in common_number:
        common_number.append(list1[i])
    i += 1
    
print(list1)
print(list2)
print(common_number)
    
# Task 3

print('\n')



number = []
i = 1
while i <= 100:
    number.append(i)
    i += 1
result = []
i = 0
while i < len(number):
    if number[i] % 7 == 0 and number[i] % 5 != 0:
        result.append(number[i])
    i += 1

print(result)


















    
    
    
    
    
    
    