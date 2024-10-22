import time

def Menu():
    while True:
        print('-' * 50)
        print('Fatorial')
        print('-' * 50)
        options = [
            '[1] Calcular Fatorial',
            '[2] Sair'
        ]
        for option in options:
            print(option)
        try:
            choice = int(input('Selecione uma opção: '))
        except ValueError:
            print('Entrada inválida. Por favor, digite um número.')
            continue
        if choice == 1:
            try:
                numero = int(input('Digite um numero: '))
                print('-' * 50)
                print(f'O fatorial de {numero} é: {Fatorial(numero)}')
                print('-' * 50)
                time.sleep(1)
            except ValueError:
                print('Entrada inválida. Por favor, digite números válidos.')
        elif choice == 2:
            break
        else:
            print('-' * 50)
            print("Opção inválida. Tente novamente.")
            print('-' * 50)
            time.sleep(1)

def Fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

Menu()