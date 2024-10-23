def Lista1():
    valores = [5, 8, 10, 3]
    dobro_valores = []

    for num in valores:
        dobro_valores.append(num *  2)
    print(valores, dobro_valores)

def Lista2():
    valores = [5, 8, 10, 3]
    dobro_valores = [num * 2 for num in valores]
    print(valores, dobro_valores)

def Lista3(): #se for par
    valores = [5, 8, 10, 3]
    dobro_valores = [num * 2 for num in valores if num %2 == 0]
    print(valores, dobro_valores)


Lista1()
Lista2()
Lista3()