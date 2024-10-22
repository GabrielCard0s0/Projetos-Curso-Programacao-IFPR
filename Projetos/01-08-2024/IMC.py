print('-'*30)
print('Calculo de IMC.')
print('-'*30)

peso = float(input('Qual o peso? '))
altura = float(input('Qual a altura? '))

imc = (altura ** 2) / peso

print('-'*30)
print(f'{imc:.2}')
print('-'*30)