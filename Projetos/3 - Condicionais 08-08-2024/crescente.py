# Exibe um cabeçalho para o programa de ordenação de números
print('-'*30)
print('Descubra a ordem crescente de dois numeros:')
print('-'*30)

# Solicita ao usuário que digite o primeiro número
num = float(input('Digite qualquer numero: '))
print('-'*30)

# Solicita ao usuário que digite o segundo número
num1 = float(input('Digite outro numero: '))
print('-'*30)

# Compara os dois números e exibe-os em ordem crescente
if num <= num1:
    print('Em ordem crescente os numeros seguem assim: ', num, num1)
    print('-'*30)
else:
    print('Em ordem crescente os numeros seguem assim: ', num1, num)
    print('-'*30)

