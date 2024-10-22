import random, time

def Digitar(texto, atraso=0.05):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(atraso)


valores = []

for e in range(100):
    valor = random.randint(0, 1000)
    valores.append(valor)

while True:
    print(valores)
    Digitar('Informe o indice:')
    try:
        indice = int(input('> '))
        print('-'*50)
        print(valores[indice-1])
        print('-'*50)
        time.sleep(1)
    except ValueError:
        Digitar('Tente uma opção válida!')