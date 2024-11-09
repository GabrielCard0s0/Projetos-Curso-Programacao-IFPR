def Obter_Lista(texto):
    while True:
        entrada = input(texto)
        try:
            # Converte a entrada em uma lista de floats
            lista = [float(num) for num in entrada.split()]
            return lista
        except ValueError:
            print("Por favor, insira apenas números separados por espaços.")

# Obtém a primeira lista
lista1 = Obter_Lista("Digite os números da primeira lista, separados por espaços: ")
# Obtém a segunda lista
lista2 = Obter_Lista("Digite os números da segunda lista, separados por espaços: ")
# Concatena as duas listas
lista_concatenada = lista1 + lista2

# Exibe a lista concatenada
print("Lista concatenada:", lista_concatenada)
