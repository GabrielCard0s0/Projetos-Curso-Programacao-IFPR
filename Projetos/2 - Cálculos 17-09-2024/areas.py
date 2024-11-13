import time

def Menu():
    while True:  # Loop principal que mantém o menu ativo
        print('-' * 50)
        print('Cálculo de Áreas')  # Título do menu
        print('-' * 50)
        
        # Opções disponíveis para o usuário
        options = [
            '[1] Calcular área do Retângulo',
            '[2] Calcular área do Triângulo',
            '[3] Calcular área do Quadrado',
            '[4] Sair'
        ]
        
        # Exibe as opções no menu
        for option in options:
            print(option)
        
        try:
            choice = int(input('Selecione uma opção: '))  # Lê a escolha do usuário
        except ValueError:
            print('Entrada inválida. Por favor, digite um número.')  # Tratamento de erro para entradas não numéricas
            continue  # Retorna ao início do loop para nova tentativa

        if choice == 1:  # Cálculo da área do retângulo
            try:
                base = float(input('Digite a base: '))  # Lê a base do retângulo
                altura = float(input('Digite a altura: '))  # Lê a altura do retângulo
                print('-' * 50)
                print(f'A área do retângulo é: {Area_Retangulo(base, altura)}')  # Calcula e exibe a área
                print('-' * 50)
                time.sleep(1)  # Pausa por um segundo
            except ValueError:
                print('Entrada inválida. Por favor, digite números válidos.')  # Tratamento de erro para entradas não numéricas

        elif choice == 2:  # Cálculo da área do triângulo
            try:
                base = float(input('Digite a base: '))  # Lê a base do triângulo
                altura = float(input('Digite a altura: '))  # Lê a altura do triângulo
                print('-' * 50)
                print(f'A área do triângulo é: {Area_Triangulo(base, altura)}')  # Calcula e exibe a área
                print('-' * 50)
                time.sleep(1)
            except ValueError:
                print('Entrada inválida. Por favor, digite números válidos.')

        elif choice == 3:  # Cálculo da área do quadrado
            try:
                lado = float(input('Digite o lado: '))  # Lê o lado do quadrado
                print('-' * 50)
                print(f'A área do quadrado é: {Area_Quadrado(lado)}')  # Calcula e exibe a área
                print('-' * 50)
                time.sleep(1)
            except ValueError:
                print('Entrada inválida. Por favor, digite um número válido.')

        elif choice == 4:  # Opção para sair
            break  # Encerra o loop e o programa

        else:  # Tratamento para opções inválidas
            print('-' * 50)
            print("Opção inválida. Tente novamente.")
            print('-' * 50)
            time.sleep(1)

# Função para calcular a área do retângulo
def Area_Retangulo(base, altura):
    return base * altura

# Função para calcular a área do triângulo
def Area_Triangulo(base, altura):
    return (base * altura) / 2

# Função para calcular a área do quadrado
def Area_Quadrado(lado):
    return lado ** 2

# Chama a função principal para iniciar o programa
Menu()
