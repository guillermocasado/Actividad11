def bubblesort(numeros):
    n = len(numeros)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if numeros[j] > numeros[j + 1]:
                aux = numeros[j + 1]
                numeros[j + 1] = numeros[j]
                numeros[j] = aux
    return numeros

class BubbleSort:
    def __init__(self, lista):
        self.sorted_list = bubblesort(lista)
