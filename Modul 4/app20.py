def medie(numbers_list):
    pass


def suma(numbers_list):
    pass

def putere(numbers_list):
    pass

meniu = {
    '1': medie,
    '2': suma,
    '3': putere
}

num_list = []
while True:
    number = input('Type a number: ').lower()
    if number == 'x':
        break
    try:
        number = float(number)
    except Exception:
        number = input('Invalid number. Type again: ')
    continue

    num_list.append(number)

methods_dist = {1: 'Media numerelor', 2: 'Suma numerelor', 3: 'Puterea numerelor', 4: 'Iesire'}
for option_number, option_number in methods_dist.items():
    print(f'{option_number}.{option_name}')

choice = input('Introduceti optiunea dvs: ')
meniu.get(choice)




