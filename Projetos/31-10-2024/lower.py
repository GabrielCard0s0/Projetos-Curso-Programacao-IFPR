import time

def Digitar(texto, atraso=0.03, pular=True):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(atraso)
    if pular == True:
        print()

while True:
    Digitar('Digite um texto ou quit para sair:')
    txt = input('> ')
    if txt == "quit":
        Digitar('Finalizando...')
        break
    else:
        Digitar('Seu texto minusculo: ',  0.03, False)
        Digitar(txt.lower())
        print()