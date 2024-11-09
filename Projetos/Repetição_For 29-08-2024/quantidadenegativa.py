import time
import sys

def main_menu():
    print('-'*30)
    print('Contar numeros negativos ?')
    print('-'*30)

    choice = input('Digite a resposta Y/N: ')

    if choice == 'y':
        time.sleep(1)
        print('-'*30)
        contar_numeros_negativos()

    elif choice == 'n':
        time.sleep(1)
        print('-'*30)
        end()

    else:
        print('Opção inválida!')
        return main_menu()

def contar_numeros_negativos():

    lista_negativos = []

    quantidade = int(input("Informe a quantidade de números que você deseja fornecer: "))

    contador_negativos = 0

    print('-'*30)
    for i in range(quantidade):
        numero = float(input(f"Informe o número {i + 1}: "))
        if numero < 0:
            contador_negativos += 1
            lista_negativos.append(numero)
            print('-'*30)
    print('-'*30)

    print(f"A quantidade de números negativos é: {contador_negativos}, e os numeros são: {lista_negativos}")
    print('-'*30)

    print('Retornando para menu...')
    time.sleep(2)
    return main_menu()

def end():
    print('Finalizando...')
    time.sleep(1)
    print('-'*30)



main_menu()