import time

def Digitar(texto, atraso=0.02):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(atraso)
    print('\n')