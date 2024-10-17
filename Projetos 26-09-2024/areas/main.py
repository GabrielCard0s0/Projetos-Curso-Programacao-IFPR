import areas.geometria as geometria, time



def Menu():
    while True:
        print('-' * 50)
        print('Calculo de Areas')
        print('-' * 50)
        options = [
            '[1] Calcular área do Retângulo',
            '[2] Calcular área do Triângulo',
            '[3] Calcular área do Quadrado',
            '[4] Calcular área do Círculo',
            '[5] Sair'
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
                print(f'A área do retângulo é: {geometria.Area_Retangulo(base, altura):.2f}')
                print('-' * 50)
                time.sleep(1)
            except ValueError:
                print('Entrada inválida. Por favor, digite números válidos.')
        elif choice == 2:
            try:
                base = float(input('Digite a base: '))
                altura = float(input('Digite a altura: '))
                print('-' * 50)
                print(f'A área do triângulo é: {geometria.Area_Triangulo(base, altura):.2f}')
                print('-' * 50)
                time.sleep(1)
            except ValueError:
                print('Entrada inválida. Por favor, digite números válidos.')
        elif choice == 3:
            try:
                lado = float(input('Digite o lado: '))
                print('-' * 50)
                print(f'A área do quadrado é: {geometria.Area_Quadrado(lado):.2f}')
                print('-' * 50)
                time.sleep(1)
            except ValueError:
                print('Entrada inválida. Por favor, digite um número válido.')
        elif choice == 4:
            try:
                raio = float(input('Digite o raio: '))
                print('-'*50)
                print(f'A área do circulo é: {geometria.Area_Circulo(raio):.2f}')
                print('-'*50)
            except ValueError:
                print('Entrada inválida. Por favor, digite um número válido.')
        elif choice == 5:
            break
        else:
            print('-' * 50)
            print("Opção inválida. Tente novamente.")
            print('-' * 50)
            time.sleep(1)

Menu()