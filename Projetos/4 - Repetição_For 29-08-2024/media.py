quantidade = int(input('informe a quantidade de numeros: '))
contagem = 0
numeros = 0

for i in range(quantidade):
    numero = float(input('Informe o numero: '))
    numeros += numero
    contagem += 1
media = numeros // contagem
print(media)
