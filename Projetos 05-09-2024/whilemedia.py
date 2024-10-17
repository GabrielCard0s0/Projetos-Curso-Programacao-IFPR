quantity = int(input('Quantidade de numeros a serem digitados: '))
total = 0
media = 0

i = 0
while i < quantity:
    number = float(input('digite o numero: '))
    total += number
    i += 1

media += total / quantity
print(f'A média é: {media}')