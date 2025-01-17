
# Task 1

def  favorite_movie(film):
  print('My favorite film: ' + film)
favorite_movie('Dedpul')
favorite_movie('Venom')


# Task 2 

def make_country(name, capital):
  country_dict = {'name': name, 'capital': capital}
  print(country_dict)

make_country('Ukraine', 'Kiev')
make_country('France', 'Paris')


# Task 3
# То как я понял задание, сделал по своиму

def make_operation(*args):
  return sum(args)
  # return_value = 0
  # for num in args:
  #   return_value += num
  # return return_value
  
print(make_operation(7, 7, 2))



def make_operation(a, b , c, d):
   print(a - b - (-c) - (-d))
  # return_value = args[0]
  # for num in args[1: ]:
  #   return_value += num
  # return return_value # Можно сделать возврат 30 будет всегда 30

make_operation(5, 5, -10, -20)


def make_operation(a,b):
  print(a*b)

make_operation(7, 6)

# Я искал и читал как можно задать в функцие весь алгаритм без усложнений
# Вот что нашел:

def make_operation(operator, *args):
  if operator == '+':
    result = sum(args)
  elif operator == '-':
    result = args[0]
    for num in args [1:]:
      result -= num
  elif operator == '*':
      result = 1
      for num in args:
        result *= num
  else:
    raise ValueError("Unsupported operator! Use '+', '-' or '*'.")
  return result

print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))

