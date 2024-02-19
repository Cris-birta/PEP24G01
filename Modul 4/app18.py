
def putere():
    while True:
        user_data1 = input()
        if user_data1 in ['Q', 'q']:
            break
        num1 = int(input())
        num2 = int(input())
        result = num1 **num2

    return result
print(putere())