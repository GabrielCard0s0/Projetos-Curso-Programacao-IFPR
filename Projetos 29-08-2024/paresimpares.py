quantidade = int(input('Digite quandos numeros irá inserir: '))
lista_pares = []
lista_impares = []


for i in range(quantidade):
    numero = int(input('digite o numero: '))
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print(f'numeros pares: {lista_pares} numeros impares: {lista_impares}')