def verificar_numero(lista, numero):
    # Verifica se o número está presente na lista
    return numero in lista

# Solicita ao usuário que digite uma lista de números
entrada = input("Digite uma lista de números separados por espaço: ")
# Converte a entrada em uma lista de inteiros
lista_numeros = list(map(int, entrada.split()))

# Solicita ao usuário um número a ser buscado na lista
numero_buscar = int(input("Digite o número a ser buscado: "))

# Verifica se o número está na lista e imprime o resultado
if verificar_numero(lista_numeros, numero_buscar):
    print(f"O número {numero_buscar} está presente na lista.")
else:
    print(f"O número {numero_buscar} não está presente na lista.")
