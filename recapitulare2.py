def functie():
    lei = [200, 100, 50, 20, 10, 5, 1]
    lst = [0, 0, 0, 0, 0, 0, 0]
    pret = int(input())
    for i in range(len(lei)):
        while pret >= lei[i]:
            pret = pret - lei[i]
            lst[i] = lst[i] + 1
    print(lei)
    print((lst),end=" ")
functie()

def fibo(n):
    if n <= 2:
        return[1]
    lf = [0] * n
    lf[0] = 0
    lf[1] = 1
    for i in range(2,n):
        lf[i] = lf[i-1] + lf[i-2]
    print(lf)

fibo(6)