import time

def Menu():
    while True:
        print('-' * 50)
        print('Calculo de Areas')
        print('-' * 50)
        options = [
            '[1] Calcular área do Retângulo',
            '[2] Calcular área do Triângulo',
            '[3] Calcular área do Quadrado',
            '[4] Sair'
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
                base = float(input('Digite a base: '))
                altura = float(input('Digite a altura: '))
                print('-' * 50)
                print(f'A área do retângulo é: {Area_Retangulo(base, altura)}')
                print('-' * 50)
                time.sleep(1)
            except ValueError:
                print('Entrada inválida. Por favor, digite números válidos.')
        elif choice == 2:
            try:
                base = float(input('Digite a base: '))
                altura = float(input('Digite a altura: '))
                print('-' * 50)
                print(f'A área do triângulo é: {Area_Triangulo(base, altura)}')
                print('-' * 50)
                time.sleep(1)
            except ValueError:
                print('Entrada inválida. Por favor, digite números válidos.')
        elif choice == 3:
            try:
                lado = float(input('Digite o lado: '))
                print('-' * 50)
                print(f'A área do quadrado é: {Area_Quadrado(lado)}')
                print('-' * 50)
                time.sleep(1)
            except ValueError:
                print('Entrada inválida. Por favor, digite um número válido.')
        elif choice == 4:
            break
        else:
            print('-' * 50)
            print("Opção inválida. Tente novamente.")
            print('-' * 50)
            time.sleep(1)

def Area_Retangulo(base, altura):
    return base * altura

def Area_Triangulo(base, altura):
    return (base * altura) / 2

def Area_Quadrado(lado):
    return lado ** 2


Menu()
