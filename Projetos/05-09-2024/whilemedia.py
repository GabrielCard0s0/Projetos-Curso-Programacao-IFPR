# Solicita ao usuário a quantidade de números a serem digitados
quantity = int(input('Quantidade de numeros a serem digitados: '))

# Inicializa as variáveis para total e média
total = 0
media = 0

# Inicializa o contador
i = 0
# Loop para ler a quantidade de números especificada
while i < quantity:
    # Solicita ao usuário que digite um número
    number = float(input('Digite o numero: '))
    total += number  # Adiciona o número ao total
    i += 1  # Incrementa o contador

# Calcula a média dos números digitados
media = total / quantity  # Corrigido para calcular média diretamente
# Exibe o resultado da média
print(f'A média é: {media}')
