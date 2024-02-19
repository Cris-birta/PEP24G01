#Functii
# def add_(x, y):
#     return x + y
# # print(x) - nu va fi printat niciodata pentru ca la functii nu se printeaza ce e in interiorul functiei
#
# result = add_(3, 4)
# print(result)

#exercitiu
#
# def factorial(x):
#     result = 1
#     for i in range(1, x+1):
#         result = result * i # e la fel cu result *= 1
#     print(result)
#
# result = factorial(4)
# print(result)

# result = 1
# def factorial(x):
#     global result
#     for i in range(1, x+1):
#         result = result * i # e la fel cu result *= 1
#
#
# factorial(4)
# print(result)


# result = 0
# def gauss(n):
#     global result
#     for i in range(1, n+1):
#         result += i
# gauss(100)
# print(result)


def sumafractii(x):
    suma = 0
    for i in range(1, x+1):
        suma += 1/i
    return suma

x = int(input())
print(sumafractii(x))