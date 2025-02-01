
# Tastk 1

class Person():

  def __init__(self, first_name, last_name, age):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age


  def talk(self):
    print(f'Hello, my name is {self.first_name} {self.last_name} and I am {self.age} years old')

person1 = Person('Carl', 'Jahnson', 26)

person1.talk()


# Task2 ------------------------------------------------

class Dog():

  age_factor = 7

  def __init__(self, dog_age):
   self.dog_age = dog_age


  def human_age(self):
    return self.dog_age * Dog.age_factor

my_dog = Dog(10)
print(my_dog.human_age())


# Task 3 ----------------------------------------------

# Список
CHANNELS = ['BBS', 'Discovery', 'TV1000']

class TVController:

  def __init__(self, channels):
    self.channels = channels
    self.current_channel = 0

  def first_channel(self):
    self.current_channel = 0 # Устанавливаем первый канал
    return self.channels[self.current_channel]
  
  def last_channel(self):
    self.current_channel = len(self.channels) - 1 # Переключаемся на последний канал и устанавливаем индекс
    return self.channels[self.current_channel]
  
  def turn_channel(self, N):
    self.current_channel = N - 1 # Используем N - 1  потому что каналы начинаеться с 1, Индексация в Петоне с 0
    return self.channels[self.current_channel]
  
  def next_channel(self): # Переход к следующему каналу (увеличиваем)
    self.current_channel = (self.current_channel + 1) % len(self.channels)
    return self.channels[self.current_channel]
  
  def previous_channel(self): # Переход к следующему каналу (Уменьшаем)
    self.current_channel = (self.current_channel - 1) % len(self.channels)
    return self.channels[self.current_channel]
  
  def get_current_channel(self): # Возвращаем
    return self.channels[self.current_channel]
  
  def exists(self, N_or_name):
        if isinstance(N_or_name, int): # Передан ли номер канала
            return "Yes" if 1 <= N_or_name <= len(self.channels) else "No"
        elif isinstance(N_or_name, str):  # Переданно ли название канала
            return "Yes" if N_or_name in self.channels else "No"
        else:
            return "No" 
        

controller = TVController(CHANNELS)

print(controller.first_channel())  
print(controller.last_channel())  
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel()) 
print(controller.get_current_channel()) 
print(controller.exists(4)) 
print(controller.exists("BBC"))
   




