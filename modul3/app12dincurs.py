# number = int(input('give number: '))
# print(True) if number > 100 else  print(False)

# number = int(input('give str: '))
#
# if test == '':
#     print

# y = int(input('year:' ))
#
# if y < 1582:
#     print('Not within Gregorian calendar')
# elif not (y % 400):
#     print('Leap year')
# elif not (y % 100):
#     print('Leap year')
# elif not (y % 4):
#     print('Leap year')
# else:
#     print('Common year')

# Problema suplimentara - Varianta 1

print('1. Cappucino....4 lei')
print('2. Expresso....3.5 lei')

option = int(input('Ce optiune alegeti? [1,2]: '))
coin = int(input('Introduceti o bancnota [5,10]: '))

# if option == 1:
#     if coin == 5:
#         rest = 5 - 4
#     elif coin == 10:
#         restr = 10 - 4
# if option == 2:
#     if coin == 5:
#         rest = 5 - 3.5
#     elif coin == 10:
#         rest = 10 - 3.5
# print(f'Veti primi restul de {rest} lei')


# Varianta 2

for opt in  '1,2':
    if int(opt) == option:
        product_value = 4
        break
    elif int(opt) == option:
        product_value = 3.5
        break
    for possible_coin in '5,10' .split(' , '):
        if coin == possible_coin:
            break
        else:
            continue
    else:
        print('not valid coin')


print(f'Veti primi restul de {float(possible_coin) - float(product_value)} lei')

