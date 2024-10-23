def Lista1():    #jeito nada elegante
    lista = [5, 8, 10, 3]

    i = 0

    while i < len(lista):
        print(lista[i])
        i += 1

def Lista2(): #jeito pythonico de escrever(elegante)
    lista = [5, 8, 10, 3]
    for num in lista:
        print(num)



Lista1()
Lista2()