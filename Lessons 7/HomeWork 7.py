# Task 1

# Строка пользователя
user = input("Enter a sentence: ")

# Преобразование строк в список
words = user.split()
word_count = {}

for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)


# Task 2


stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_prices = {}
for item in stock:
  total_prices[item] = stock[item] * prices[item]

# Вывел в столбик
# Эксперемент ( проба)
for item, total_price in total_prices.items():
    print(f"{item}: {total_price}")


# Task 3

result = [(i, i**2) for i in range(1, 10)]
print(result)

# Task 4


day = ["Monday", "Tuesday", "Wednesday", "Thursday",
                 "Friday", "Saturday", "Sunday"]

day_to_number = {i+1: day for i, day in enumerate(day)}
number_to_day = {day: i+1 for i, day in enumerate(day)}

# Может ли считаться такие столбцы правильными?????? (Можно пожалуйста коментарий на это)
# Мои эксперементы.

for item in day_to_number.items():
    print(item)

for item in number_to_day.items():
    print(item)

# print(day_to_number)
# print(number_to_day)