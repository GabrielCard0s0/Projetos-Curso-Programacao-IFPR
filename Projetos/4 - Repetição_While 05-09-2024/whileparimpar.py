# Solicita ao usuário a quantidade de números a serem digitados
quantity = int(input('Quantidade de numeros a serem digitados: '))

# Inicializa listas para armazenar números pares e ímpares
lista_pares = []
lista_impares = []

# Inicializa contadores para números pares e ímpares
pares = 0
impares = 0

# Inicializa o contador
i = 0
# Loop para ler a quantidade de números especificada
while i < quantity:
    # Solicita ao usuário que digite um número
    number = float(input('Digite o numero: '))
    # Verifica se o número é par
    if number % 2 == 0:
        pares += 1  # Incrementa o contador de pares
        lista_pares.append(number)  # Adiciona o número à lista de pares
    else:
        impares += 1  # Incrementa o contador de ímpares
        lista_impares.append(number)  # Adiciona o número à lista de ímpares
    i += 1  # Incrementa o contador

# Exibe a quantidade de números pares e ímpares, além das respectivas listas
print(f'Quantidade de pares: {pares}, ímpares: {impares}, são eles pares: {lista_pares}, ímpares: {lista_impares}')
