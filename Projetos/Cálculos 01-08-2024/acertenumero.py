import random  # Importa a biblioteca random para gerar números aleatórios

# Solicita ao usuário que digite um número de 1 a 10
numero1a10 = float(input('Digite um numero de 1 a 10\n'))

# Gera um número aleatório entre 1 e 10 (exclusivo)
gerar1a10 = random.randrange(1, 10)

# Verifica se o número digitado pelo usuário é igual ao número gerado
if numero1a10 == gerar1a10:
    print('-'*30)
    print('Você acertou! O número correto é:\n', gerar1a10)  # Informa que o usuário acertou
    print('-'*30)
else:
    print('-'*30)
    print('Você errou! O número correto é:\n', gerar1a10)  # Informa que o usuário errou
    print('-'*30)
