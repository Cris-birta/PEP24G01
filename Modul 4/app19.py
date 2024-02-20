number_of_participants = int(input('Type the number of participants: '))
ages = []
for i in range(1, number_of_participants+1):
    try:
        age = int(input('Type the age of participants: '))
    except ValueError:
        age = int(input(f'Invalid format of the participants {i}. Type again: '))
    ages.append(age)

#new
def avg(list_of_numbers):
    # total = 0
    # for age in list of numbers:
    #     total+= age
    total = sum(list_of_numbers)
    average_age = total / len(list_of_numbers)
    return average_age

print(avg(ages))



