def Lista1():
    # Define uma lista de valores
    valores = [5, 8, 10, 3]
    dobro_valores = []  # Lista para armazenar o dobro dos valores

    # Itera sobre cada número na lista original
    for num in valores:
        dobro_valores.append(num * 2)  # Adiciona o dobro do número na nova lista
    print(valores, dobro_valores)  # Exibe a lista original e a lista com os valores dobrados

def Lista2():
    # Define uma lista de valores
    valores = [5, 8, 10, 3]
    # Usando compreensão de lista para criar uma nova lista com o dobro dos valores
    dobro_valores = [num * 2 for num in valores]
    print(valores, dobro_valores)  # Exibe a lista original e a lista com os valores dobrados

def Lista3():  # Cria uma lista apenas com os valores pares dobrados
    # Define uma lista de valores
    valores = [5, 8, 10, 3]
    # Usando compreensão de lista com condição para filtrar apenas números pares
    dobro_valores = [num * 2 for num in valores if num % 2 == 0]
    print(valores, dobro_valores)  # Exibe a lista original e a lista com os valores pares dobrados

# Chama as funções para executar
Lista1()
Lista2()
Lista3()
