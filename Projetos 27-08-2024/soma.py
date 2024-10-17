import math
import sys
import time


def Menu_principal():
    print(f'1. Somar\n 2. Subtrair\n  3.Sair\n')
    print('-'*30)
    choice = int(input('Digite a opção: '))
    if choice == 1:
        print('-'*30)
        Add()
    elif choice ==2:
        print('-'*30)
        Sub()  
    elif choice == 3:
        print('-'*30)
        Sair()
    else:
        print('-'*30)
        print('Opção invalida!. Tente novamente')
        print('-'*30)
        return Menu_principal()
def Add():
    total = 0
    choice = int(input('Quantos numeros serão subtraidos:'))
    for i in range(choice):
        numb = float(input('digite um numero: '))
        total += numb
    print(f'Soma total: {total}')
    return Add()

def Sub():
    sub = 0
    choice = int(input('Quantos numeros serão somados:'))
    for i in range(choice):
        numeros = float(input('digite um numero: '))
        sub -= numeros
    print(f'Total: {sub}')
    return Sub()

def Sair():
    print('-'*30)
    print(f'Finalizando...')
    print('-'*30)
    time.sleep(1)
    sys.exit


Menu_principal()    