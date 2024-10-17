import math
import sys
import time


def Main_Menu():
    print(f'1. Fatorial\n 2.Sair\n')
    print('-'*30)
    choice = int(input('Digite a opção: '))
    if choice == 1:
        print('-'*30)
        Multiply()
    elif choice == 2:
        print('-'*30)
        Sair()
    else:
        print('-'*30)
        print('Opção invalida!. Tente novamente')
        print('-'*30)
        return Main_Menu()
    
def Multiply():
    resultado = 1
    numb = int(input('Digite um numero inteiro: '))
    for i in range(1, numb + 1):
        resultado *= i
    print('-'*30)    
    print(f'o resultado fatorial de {numb} é: {resultado}')
    print('-'*30)
    time.sleep(1)
    return Main_Menu()


def Sair():
    print('-'*30)
    print(f'Finalizando...')
    print('-'*30)
    time.sleep(1)
    sys.exit

Main_Menu()    
