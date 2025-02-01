
# Task 1

# def logger(func):
#   def wrapper(*args, **kwargs):
#     print(f'argument: {args} argument2: {kwargs}')
#     return func(*args, **kwargs)
#   return wrapper

# @logger
# def add(x, y):
#     return x + y

# @logger
# def square_all(*args):
#     return [arg ** 2 for arg in args]

# print(add(4 ,5))
# print(square_all(1, 2, 3))

# Task 2


def stop_words(words: list):
   def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for word in words:
                result = result.replace(word, '*' * len(word))
            return result
        return wrapper
   return decorator




@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"



# assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
print(create_slogan("Steve"))

# Task 3

# max_length: 15
# type_: str
# contains: []  - list of symbols that an argument should contain

def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            
    




@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"




assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

