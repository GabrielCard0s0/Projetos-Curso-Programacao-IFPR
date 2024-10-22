quantity = int(input('Quantidade de numeros a serem digitados: '))
lista_negativos = []
negatives = 0

i = 0
while i < quantity:
    number = float(input('digite o numero: '))
    if number < 0:
        negatives += 1
        lista_negativos.append(number)
    i += 1
print(f'Quantidade de negativos: {negatives}, são eles: {lista_negativos}')