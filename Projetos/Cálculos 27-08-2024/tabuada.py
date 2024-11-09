import math
import sys
import time

def Menu_principal():
    print(f'1. Ver a tabuada:', '\n 3. Sair')
    print('-'*30)
    choice = int(input('Digite a opção: '))
    if choice == 1:
        print('-'*30)
        Tabuada()
    elif choice == 3:
        print('-'*30)
        Sair()
    else:
        print('-'*30)
        print('Opção invalida!. Tente novamente')
        print('-'*30)

def Tabuada():
    print('-'*30)
    numero = int(input('Digite um numero: '))
    print(f'Tabuada do {numero}:')
    print('-'*30)
    for i in range(0, 11):
        resultado = numero * i
        print(f'{numero} x {i} = {resultado}')
    print('-'*30)
    time.sleep(1)    
    return Menu_principal()
    
def Sair():
    print('-'*30)
    print(f'Finalizando...')
    print('-'*30)
    time.sleep(1)
    sys.exit

Menu_principal()    