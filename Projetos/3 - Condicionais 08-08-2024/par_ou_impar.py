# Exibe um cabeçalho para o programa de verificação de par ou ímpar
print('-'*30)
print('Descubra se o número é par ou ímpar:')
print('-'*30)

# Solicita ao usuário que digite um número inteiro
num = int(input('Digite um numero inteiro: '))

# Verifica se o número é par
if num % 2 == 0:  # Correção: deve usar o operador % para verificar se o resto da divisão é 0
    print('-'*30)
    print(num, 'é par!')
    print('-'*30)
else:
    print('-'*30)
    print(num, 'é ímpar!')
    print('-'*30)
