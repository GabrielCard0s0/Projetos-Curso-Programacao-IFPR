import math
import sys
import time


def Menu_principal():
    print(f'1. Menor numero de uma sequencia \n  2.Sair\n')
    print('-'*30)
    choice = int(input('Digite a opção: '))
    if choice == 1:
        print('-'*30)
        Sequencia()

    elif choice == 2:
        print('-'*30)
        Sair()
    else:
        print('-'*30)
        print('Opção invalida!. Tente novamente')
        print('-'*30)
        return Menu_principal()
    
def Sequencia():
    num = []
    choice = int(input('Digite a quantidade de numeros da sequencia: '))
    for i in range(choice):
        num.append(float(input('digite um numero: ')))
    num.sort()
    print('sequencia crescente:', num, ', o menor numero é', num[0])


def Sair():
    print('-'*30)
    print(f'Finalizando...')
    print('-'*30)
    time.sleep(1)
    sys.exit


Menu_principal()    