from bubble_sort import BubbleSort
lista = []
posicion1 = True
while True:
    cifra = input('Dime un numero entero: ')

    try:
        int(cifra)
        if  int(cifra) == -9999:
            bubble = BubbleSort(lista)
            print(bubble.sorted_list)
            del bubble
            lista.clear()
            posicion1 = True
        else:
            lista.append(int(cifra))
            posicion1 = False
    except ValueError:
        print('El dato introducido no es un número entero: ')
        if cifra.lower() == "fin":
            if posicion1:
                break


