# def functie(n):
#     list = [1, 2, 3, 4, 5]
#     for i in range(len(list)):
#         if list[i] == n:
#             return True
#     return False
#
#
# print(functie(9))


def factorial(n):
    if n < 10:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(12))