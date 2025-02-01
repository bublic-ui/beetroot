
# Task 1 

class Person():


  def __init__(self,name,age):
    self.name = name
    self.age = age
  def introduce(self):
     return (f"Hello, my name is {self.name} and I am {self.age} years old")

class Student(Person):
  def __init__(self, name, age, grade):
     super().__init__(name, age)
     self.grade = grade
  def study(self):
     return f'{self.name} is studying.'
  def introduce(self):
     return (f'Hello, my name is {self.name}, I am {self.age} years old, and I am in grade {self.grade}.')
  

class Teacher(Person):
    def __init__(self, name, age, salary):
       super().__init__(name, age)
       self.salary = salary
    def teach(self):
       return f'{self.name} is teaching.'
    def introduce(self):
       return f'Hello, my name is {self.name}, I am {self.age} years old, and I earn a salary of {self.salary}.'
    

student1 = Student("John", 16, 10)
student2 = Student("Alice", 17, 11)


teacher1 = Teacher("Mr. Smith", 40, 50000)
teacher2 = Teacher("Ms. Johnson", 35, 55000)

print(student1.introduce())
print(student2.study())

print(teacher1.introduce())
print(teacher2.teach())


# Task 2 --------------------------------------------------


class Mathematician():
   
   def square_nums(self, nums):
      """принимает список и возвращает квадратов чисел"""
      return [num ** 2 for num in nums]
   def remove_positives(self, nums):
      """возвращает буз положительного числа"""
      return[num for num in nums if num <= 0]
   def filter_leaps(self, years):
      """принимает список говод и возвращает высокосный"""
      def is_leap_year(year):
         return (year%4 == 0 and year % 100 != 0) or (year%400 == 0)
      return[year for year in years if is_leap_year(year)]
   
m = Mathematician()

print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90]))
print(m.filter_leaps([2001, 2022, 2004]))

# Task 3 ----------------------------------------------------------





          




