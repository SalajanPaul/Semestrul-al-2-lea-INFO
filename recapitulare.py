def functie(n):
    list = [1, 2, 3, 4, 5]
    for i in range(len(list)):
        if list[i] == n:
            return True
    return False

print(functie(9))


def factorial(n):
    if n < 10:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(12))


def bubble_sort(n):
    for i in range(len(n)):
        for j in range(len(n)-i-1):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]

n = [1,6,8,7,2]

print(bubble_sort(n))
print(n)