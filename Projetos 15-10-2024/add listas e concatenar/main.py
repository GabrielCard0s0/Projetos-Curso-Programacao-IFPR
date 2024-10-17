def Obter_Lista(prompt):
    while True:
        entrada = input(prompt)
        try:
            lista = [float(num) for num in entrada.split()]
            return lista
        except ValueError:
            print("Por favor, insira apenas números separados por espaços.")


lista1 = Obter_Lista("Digite os números da primeira lista, separados por espaços: ")
lista2 = Obter_Lista("Digite os números da segunda lista, separados por espaços: ")
lista_concatenada = lista1 + lista2

print("Lista concatenada:", lista_concatenada)
