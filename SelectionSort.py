def selectionShort(itemsList):
    n = len(itemsList)
    for i in range(n):
        minValueIndex = i

        for j in range(i + 1, n):
            if itemsList[j] < itemsList[minValueIndex]:
                minValueIndex = j

        if minValueIndex != i:
            temp = itemsList[i]
            itemsList[i] = itemsList[minValueIndex]
            itemsList[minValueIndex] = temp


    return itemsList


data = [5, 1, 10, 2, 9]
selectionShort(data)
print("sorted")
print(data)


def cautare_lista(lista, nr):
    for i in range(len(lista)):
        if lista[i] == nr:
            print(nr)

cautare_lista([2,3,4,5,6],8)