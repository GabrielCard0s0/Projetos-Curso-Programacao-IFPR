import math
import sys
import time

def Main_Menu():
    print(f'\n------------------------------------''\n1. Digitar um numero e saber se ele é impar', '\n 2. Saber numeros pares entre 1 e 50', '\n 3. Sair')
    print('-'*30)
    choice = int(input('Digite a opção: '))
    if choice == 1:
        Numero_Impar()
    elif choice == 2:
        Impar_1a50()
    elif choice == 3:
        Sair()
    else:
        print('Opção invalida!. Tente novamente')

def Numero_Impar():
    print('-'*30)
    choice = int(input('Digite um numero: '))
    if choice % 2 == 1:
        print(f'{choice} é um número impar.')
    else:
        print(f'{choice} é um número par.')
    print('-'*30)
    return Main_Menu()

def Impar_1a50():
    print('-'*30)
    for num in range(1, 50, 2):
        print(f'{num}')
    return Main_Menu()
    
def Sair():
    print('-'*30)
    print(f'Finalizando...')
    print('-'*30)
    time.sleep(1)
    sys.exit

Main_Menu()    