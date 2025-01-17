

print('\n')


s = [1, 2, 3, 4]

a = [1, '1', 3.0]

print(s)
print(a)

print('\n')

d_tuple = (1, 2, 3)
w_tuple = (1, '1', 3.0)

print(w_tuple)

print('\n')

test_list = [ 19, 6, 3, 10, 8, 2, 2, 6, 1, 10, 10, 6]
print( 'Number of 6 digits in list: ', test_list.count (6))
print('Index of first accurance of digit 3 in list: ', test_list.index (3))



print('\n')

print(test_list[0]) # index from O
print(test_list[1])
print(test_list[1:4])
print(test_list[::2])


print('\n')


x = [1,2,3] 
y = (1,2,3)
x[1] = 101
print (x)

print('\n')



l = [1, 2, 3, 4, 5]

# l.append(7) принимает только один символ
# l.extend ([6,7]) расширивает список
# l.pop выводит стан 
print('\n')

x = l.pop()
print(l)

print(x)


print('\n')

range_len = 10
range_obj = range(range_len)
i = 0
while i < range_len:
    print(range_obj[i])
    i += 1


print('\n')


range_len = 10
range_obj = range(range_len)
i = 0
t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while i < range_len:
    print(range_obj[i], t[i])
    i += 1

print('\n')



l = [1, 2, 3, 4]
for i in range(len(l)):
    print(l[i])





print('\n')


range_len = [10]
for i in range(len(range_len)):
    print(range_len[i])

print('\n')


browsers = ['Chrome', 'Safary', 'FireFox', 'Edge']

print("My favorite is : " + browsers[3])

print('\n')


browsers = ['Chrome', 'Safary', 'FireFox', 'Edge']
browsers.append('Opera')
print(browsers)

print('\n')

browsers = ['Chrome', 'Safary', 'FireFox', 'Edge']
browsers.extend(['Opera', 'Exploer'])
print(browsers)

print('\n')



browsers = ['Chrome', 'Safary', 'FireFox', 'Edge']
browsers.insert(0, 'Opera')

print(browsers)


print('\n')


browsers = ['Chrome', 'Safary', 'FireFox', 'Edge']
popped_item = browsers.pop(1)
print(browsers)
print(popped_item)


# ----------


print('\n')

browsers = ['Chrome', 'Safary', 'FireFox', 'Edge']
del browsers[1]
print(browsers)

print('\n')

browsers = ['Chrome', 'Safary', 'FireFox', 'Edge']
browsers.remove('Edge')
print(browsers)


# ----------


print('\n')

browsers = ['Chrome', 'Safary', 'FireFox', 'Edge']
print(browsers)

browsers.sort()
print(browsers)

#----------

print('\n')

browsers = ['Chrome', 'Safary', 'FireFox', 'Edge']
print(browsers)

browsers.reverse()
print(browsers)

# ---------

print('\n')

countris = {'Norwegia', 'Sweden', 'Demark'}
print('Norwegia' in countris)












