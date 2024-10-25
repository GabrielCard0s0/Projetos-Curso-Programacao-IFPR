def Lista1():  # Método menos elegante para percorrer a lista
    lista = [5, 8, 10, 3]  # Define uma lista de números

    i = 0  # Inicializa um contador

    # Usa um loop while para iterar sobre os elementos da lista
    while i < len(lista):
        print(lista[i])  # Imprime o elemento atual
        i += 1  # Incrementa o contador

def Lista2():  # Método mais "pythônico" para percorrer a lista
    lista = [5, 8, 10, 3]  # Define uma lista de números
    # Usa um loop for para iterar diretamente sobre os elementos da lista
    for num in lista:
        print(num)  # Imprime cada número

# Chama as funções para executar
Lista1()
Lista2()
