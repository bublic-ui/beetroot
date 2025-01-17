# countries = ['Ukraina', 'Belarus', 'France', 'Germani',
#              'Estonia', 'Poland', 'Finland', 'Serbia']
# for i, country in enumerate(countries):
#      countries[i] = (country, i + 1)
# print(countries)

# ----------------------------------------------------------

# print('\n')

sevens = []

for i in range(1, 71, ):
     if i % 7 == 0:
          sevens.append(i)
print(sevens)

# --------------------------------------------------------
# print('\n')

# sevens = []

# for i in range(0, 71, 7):
#       sevens.append(i)
# print(sevens)


# --------------------------------------------------------
# print('\n')

# sevens = []
# i = 0

# while i < 70:
#   sevens.append(i)
#   i += 7
# print(sevens)

# ---------------------------------------------------------

# print('\n')

# import random

# points = 0
# while True: 
#   x = random.randint(0, 10)
#   y = random.randint(0, 10)
#   print('points: ' + str(points))
#   answer = input(str(x) + '+' + str(y) + '=? (type q to quit): ')
#   if answer == 'q':
#     break
#   elif int(answer) != x + y:
#     print('Not points for you')
#     continue 
# print('God job')
# points += 1


# -----------While - это список вниз----------------------------------------------------------

# print('\n')

# a_list = [1, 2, 3, 4, 5, 6, 7]

# i = 0
# while i < len(a_list):
#   print(a_list[i])
#   i += 1

# --------------------------------------------------------------------------

# print('\n')

# a_list = [1, 2, 3, 4, 5, 6, 7]

# i = 0
# for item in a_list:
#   print(item)

# ---------------------------------------------------------------------------



# a_list = [1, 2, 3, 4, 5, 6, 7]

# i = 0

# for ind, item in enumerate(a_list):
#   print(ind, item)

# ---------------------------------------------------------------------------


# a_list = [1, 2, 3, 4, 5, 6, 7]

# i = 0

# for i in range(len(a_list)):
#   print(a_list[i])

# --------------------------------------------------------------------------


# a_list = [1, 2, 3, 4, 5, 6, 7]

# i = 0

# for item in a_list:
#   if item == 2:
#     break # continuem # Убирает или останавливаеться после заданого числа
# print(item)