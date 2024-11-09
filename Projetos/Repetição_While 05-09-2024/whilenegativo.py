# Solicita ao usuário a quantidade de números a serem digitados
quantity = int(input('Quantidade de numeros a serem digitados: '))

# Inicializa uma lista para armazenar os números negativos
lista_negativos = []
# Inicializa um contador para os números negativos
negatives = 0

# Inicializa o contador
i = 0
# Loop para ler a quantidade de números especificada
while i < quantity:
    # Solicita ao usuário que digite um número
    number = float(input('Digite o numero: '))
    # Verifica se o número é negativo
    if number < 0:
        negatives += 1  # Incrementa o contador de negativos
        lista_negativos.append(number)  # Adiciona o número negativo à lista
    i += 1  # Incrementa o contador

# Exibe a quantidade de números negativos e a lista deles
print(f'Quantidade de negativos: {negatives}, são eles: {lista_negativos}')
