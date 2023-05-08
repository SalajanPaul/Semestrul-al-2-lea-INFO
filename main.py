def functie(lista, n):
    for i in range(len(lista)):
        if list[i] == n:
            return True
    return False
functie([4,5,6,7], 5)

def matriceEX(matrice, n):
    r = len(matrice)
    c = len(matrice[0])
    for i in range(r):
        for j in range(c):
            if matrice[i][j] == n:
                return True
    return False