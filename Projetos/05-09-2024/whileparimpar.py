quantity = int(input('Quantidade de numeros a serem digitados: '))
lista_pares = []
lista_impares = []
pares = 0
impares = 0

i = 0
while i < quantity:
    number = float(input('digite o numero: '))
    if number % 2 == 0:
        pares += 1
        lista_pares.append(number)
    else:
        impares += 1
        lista_impares.append(number)
    i += 1
print(f'Quantidade de pares: {pares}impares: {impares}, são eles pares: {lista_pares}impares: {lista_impares}')