def Menu():
    while True:  # Loop principal que mantém o menu ativo
        print('-' * 50)
        print('Índice de Massa Corporal')  # Título do menu
        print('-' * 50)
        
        # Opções disponíveis para o usuário
        options = ['[1] Calcular IMC', '[2] Sair']
        
        # Exibe as opções no menu
        for option in options:
            print(option)
        
        try:
            print('Selecione uma opção:')
            choice = int(input('> '))  # Lê a escolha do usuário
        except (ValueError, TypeError):
            print("Opção inválida. Tente novamente.")  # Tratamento de erro para entradas não numéricas
            continue  # Retorna ao início do loop para nova tentativa

        if choice == 1:  # Opção para calcular IMC
            try:
                p = float(input('Digite o peso (kg): '))  # Lê o peso do usuário
                h = float(input('Digite a altura (m): '))  # Lê a altura do usuário
                print('-' * 50)
                IMC, grau = I_M_C(p, h)  # Chama a função para calcular IMC
                print(f'O IMC é: {IMC:.2f}')  # Exibe o IMC formatado com duas casas decimais
                print(f'Grau IMC: {grau}')  # Exibe a classificação do IMC
                print('-' * 50)
            except (ValueError, TypeError):
                print("Entrada inválida. Tente novamente.")  # Tratamento de erro para entradas não numéricas
                continue
        
        elif choice == 2:  # Opção para sair
            break  # Encerra o loop e o programa
        
        else:  # Tratamento para opções inválidas
            print("Opção inválida. Tente novamente.")

def I_M_C(peso, altura):
    # Classificações de IMC
    baixo_peso = 'Baixo peso'
    peso_normal = 'Peso normal'
    sobrepeso = 'Sobrepeso'
    obesidade_1 = 'Obesidade grau 1'
    obesidade_2 = 'Obesidade grau 2'
    
    total = peso / (altura ** 2)  # Cálculo do IMC
    
    # Determina a classificação com base no valor do IMC
    if total < 18.5:
        grau = baixo_peso
    elif 18.5 <= total < 25:
        grau = peso_normal
    elif 25 <= total < 30:
        grau = sobrepeso
    elif 30 <= total < 40:
        grau = obesidade_1
    else:
        grau = obesidade_2
    
    return total, grau  # Retorna o valor do IMC e a classificação

# Chama a função principal para iniciar o programa
Menu()
