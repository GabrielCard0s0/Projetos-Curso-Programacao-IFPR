import math
import sys
import time

def Menu_principal():
    print(f'1. Somar', '\n 3. Sair')
    print('-'*30)
    choice = int(input('Digite a opção: '))
    if choice == 1:
        print('-'*30)
        Soma()
    elif choice == 3:
        print('-'*30)
        Sair()
    else:
        print('-'*30)
        print('Opção invalida!. Tente novamente')
        print('-'*30)

def Soma():
    choice = int(input('Quantidade de numeros a serem somados: '))
    for i in range(choice):
        print(choice)
    return Menu_principal()


def Sair():
    print('-'*30)
    print(f'Finalizando...')
    print('-'*30)
    time.sleep(1)
    sys.exit

Menu_principal()    