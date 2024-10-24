# Solicita ao usuário que digite um número para verificar se é primo
print(f'Digite um número para saber se ele é primo:')
number = int(input('> '))
divisor = 0  # Inicializa o contador de divisores

# Inicializa o contador para verificar todos os números de 1 até o número fornecido
i = 1
while i <= number:
    # Verifica se i é um divisor do número
    if number % i == 0:
        divisor += 1  # Incrementa o contador de divisores
    i += 1  # Incrementa i para verificar o próximo número

# Um número é primo se tiver exatamente 2 divisores: 1 e ele mesmo
if divisor == 2:      
    print(f'{number} é primo.')
else:
    print(f'{number} não é primo.')
