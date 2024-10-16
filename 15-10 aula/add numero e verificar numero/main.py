
def verificar_numero(lista, numero):
    return numero in lista


entrada = input("Digite uma lista de números separados por espaço: ")
lista_numeros = list(map(int, entrada.split()))


numero_buscar = int(input("Digite o número a ser buscado: "))


if verificar_numero(lista_numeros, numero_buscar):
    print(f"O número {numero_buscar} está presente na lista.")
else:
    print(f"O número {numero_buscar} não está presente na lista.")

