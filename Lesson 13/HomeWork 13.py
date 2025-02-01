
# Task 1
def function():
    a = 10
    b = 20
    c = 30
    result = a + b + c
    return result

def logger_func(func):
    return func.__code__.co_nlocals

print(logger_func(function))

# Task 2

def user(test):
    print ('Hello man')
    test()
    print('New York')
  
def logo_user():
    print('I am SpiderMan')

user(logo_user)

# Task 3


def choose_func(nums: list, func1, func2):
    logger_func = list(filter(lambda num: num > 0, nums))
    if len(logger_func) == len(nums):
        return func1(nums)
    else:
        return func2(nums)
    
    # for num in nums:
    #     if num <= 0:
    #         return func2(nums)
    # return func1(nums)
 

# Assertions

nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]

 

def square_nums(nums):

    return [num ** 2 for num in nums]

 

def remove_negatives(nums):

    return [num for num in nums if num > 0]

 

print(choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25])

print(choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5])


