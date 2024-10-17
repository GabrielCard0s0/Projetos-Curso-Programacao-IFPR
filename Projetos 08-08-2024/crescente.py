print('-'*30)
print('Descubra a ordem crescente de dois numeros:')
print('-'*30)

num = float(input('Digite qualquer numero: '))
print('-'*30)
num1 = float(input('Digite outro numero: '))
print('-'*30)

if num <= num1:
    print('Em ordem crescente os numeros seguem assim: ', num, num1)
    print('-'*30)
else:
    print('Em ordem crescente os numeros seguem assim: ', num1, num)
    print('-'*30)