def Menu():
    while True:  # Loop principal que mantém o menu ativo
        print('-' * 50)
        print('Área do Retângulo')  # Título do menu
        print('-' * 50)
        
        # Opções disponíveis para o usuário
        options = ['[1] Calcular área do Retângulo', '[2] Sair']
        for option in options:
            print(option)
        
        try:
            print('Selecione uma opção:')
            choice = int(input('> '))  # Lê a escolha do usuário
        except (ValueError, TypeError):  # Tratamento de erro para entradas não numéricas
            continue  # Retorna ao início do loop para nova tentativa

        if choice == 1:  # Opção para calcular área do retângulo
            try:
                b = float(input('Digite a base: '))  # Lê a base do retângulo
                h = float(input('Digite a altura: '))  # Lê a altura do retângulo
                A = 0  # Inicializa a variável área
                print('-' * 50)
                # Chama a função para calcular a área
                print(f'A área do retângulo é: {Area_Retangulo(A, b, h)}')  
                print('-' * 50)
            except (ValueError, TypeError):  # Tratamento de erro para entradas não numéricas
                continue  # Retorna ao início do loop para nova tentativa
        else:
            break  # Encerra o loop se a opção for diferente de 1

def Area_Retangulo(Area, base, altura):
    parcial = base * altura  # Cálculo da área do retângulo
    Area = parcial  # Atribui o valor calculado à variável Area
    return Area  # Retorna o valor da área

# Chama a função principal para iniciar o programa
Menu()
