##Task 1

name = 'Volodymyr'
last_name = 'Poliakov'
day = 'Friday'

# Метод 1
print(f'Good day {name} {last_name}! {day} is a perfect day to learn some python.')


print('\n')

# Метод 2
s = 'Good day {} {}! {} is a perfect day to learn some python.'

print(s.format(name,last_name,day))


print('\n')

# Метод 3
print('Good day %s %s! %s is a perfect day to learn some python.' %(name,last_name,day))


