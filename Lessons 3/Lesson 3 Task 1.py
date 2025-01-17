# Task 1

print('\n')




data = 'helloworld'

if len(data) < 2:
    print('')
else:
    print(data[:2]+ data[-2:])


print('\n')


data2 = 'my'


if len(data2) < 2:
    print('')
else:
    print(data2 + data2)
    
print('\n')

data3 = 'x'

if len(data3) < 2:
    print('')
else:
    print(data3)
    
# Task 2

number_phone = "1934767890"  
# .isdigit() проверяет в строке (number_phone) являеться ли это цифры
if len(number_phone) == 10 and number_phone.isdigit():
    print(number_phone)
else:
    print("Invalid phone number")
    
print('\n')

# Task 3

e = "2 + 6"
c = eval(e)

user = input(f"What is {e}? ")

if user.isdigit() and int(user) == c:
    print("Correct.")
else:
    print(f"Incorrect. The correct answer is {c}.")
    
print('\n')

# Task 4

name = "volodymyr"

user = input('Enter your name: ')
if user.lower() == name:
    print(True)
else:
    print(False)













