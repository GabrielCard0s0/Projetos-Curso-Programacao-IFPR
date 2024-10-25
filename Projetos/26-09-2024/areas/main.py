import areas.geometria as geometria  # Importa o módulo de geometria
import time  # Importa o módulo time para pausar a execução

def Menu():
    while True:
        print('-' * 50)
        print('Cálculo de Áreas')  # Cabeçalho do menu
        print('-' * 50)
        options = [
            '[1] Calcular área do Retângulo',
            '[2] Calcular área do Triângulo',
            '[3] Calcular área do Quadrado',
            '[4] Calcular área do Círculo',
            '[5] Sair'
        ]
        # Exibe as opções do menu
        for option in options:
            print(option)
        
        try:
            choice = int(input('Selecione uma opção: '))  # Lê a escolha do usuário
        except ValueError:
            print('Entrada inválida. Por favor, digite um número.')  # Trata erro de entrada
            continue

        # Calcula a área do retângulo
        if choice == 1:
            try:
                base = float(input('Digite a base: '))  # Lê a base
                altura = float(input('Digite a altura: '))  # Lê a altura
                print('-' * 50)
                print(f'A área do retângulo é: {geometria.Area_Retangulo(base, altura):.2f}')  # Chama a função e exibe o resultado
                print('-' * 50)
                time.sleep(1)  # Pausa para melhor visualização
            except ValueError:
                print('Entrada inválida. Por favor, digite números válidos.')

        # Calcula a área do triângulo
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

        # Calcula a área do quadrado
        elif choice == 3:
            try:
                lado = float(input('Digite o lado: '))
                print('-' * 50)
                print(f'A área do quadrado é: {geometria.Area_Quadrado(lado):.2f}')
                print('-' * 50)
                time.sleep(1)
            except ValueError:
                print('Entrada inválida. Por favor, digite um número válido.')

        # Calcula a área do círculo
        elif choice == 4:
            try:
                raio = float(input('Digite o raio: '))
                print('-' * 50)
                print(f'A área do círculo é: {geometria.Area_Circulo(raio):.2f}')
                print('-' * 50)
            except ValueError:
                print('Entrada inválida. Por favor, digite um número válido.')

        # Sair do programa
        elif choice == 5:
            break
        
        else:
            print('-' * 50)
            print("Opção inválida. Tente novamente.")  # Caso a opção não seja válida
            print('-' * 50)
            time.sleep(1)

Menu()  # Chama a função principal para iniciar o menu
