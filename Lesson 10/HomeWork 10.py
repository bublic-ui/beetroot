
# Task 1

def oops():
  raise IndexError ('This is an IndexError')
  # print('World')


def hi_oops():
  try:
    oops()
  except IndexError:
    print('Hello')
  except TypeError:
    print('oops spam')
  except KeyError:
    print('OWWWWwww')
hi_oops()

def oops():
   raise KeyError('This is an KeyError')
  # print('City')

hi_oops()



# Task 2

def user():
        a = float(input("Enter number a: "))
        b = float(input("Enter number b: "))
        result = (a ** 2) / b
        print(result)
        # return result

def hi_user():
   try:
      user()
   except ZeroDivisionError:
      print('Cannot divide by zero')
   except ValueError:
      print('Only numbers!')
hi_user()
