import time

def Menu():
    while True:  # Loop principal que mantém o menu ativo
        print('-' * 50)
        print('Fatorial')  # Título do menu
        print('-' * 50)
        
        # Opções disponíveis para o usuário
        options = [
            '[1] Calcular Fatorial',
            '[2] Sair'
        ]
        
        # Exibe as opções no menu
        for option in options:
            print(option)
        
        try:
            choice = int(input('Selecione uma opção: '))  # Lê a escolha do usuário
        except ValueError:
            print('Entrada inválida. Por favor, digite um número.')  # Tratamento de erro para entradas não numéricas
            continue  # Retorna ao início do loop para nova tentativa

        if choice == 1:  # Opção para calcular fatorial
            try:
                numero = int(input('Digite um número: '))  # Lê o número do qual calcular o fatorial
                print('-' * 50)
                print(f'O fatorial de {numero} é: {Fatorial(numero)}')  # Calcula e exibe o fatorial
                print('-' * 50)
                time.sleep(1)  # Pausa por um segundo
            except ValueError:
                print('Entrada inválida. Por favor, digite números válidos.')  # Tratamento de erro para entradas não numéricas

        elif choice == 2:  # Opção para sair
            break  # Encerra o loop e o programa

        else:  # Tratamento para opções inválidas
            print('-' * 50)
            print("Opção inválida. Tente novamente.")
            print('-' * 50)
            time.sleep(1)

# Função para calcular o fatorial de um número
def Fatorial(numero):
    resultado = 1  # Inicializa o resultado
    for i in range(1, numero + 1):  # Loop de 1 até o número incluído
        resultado *= i  # Multiplica o resultado pelo número atual
    return resultado  # Retorna o fatorial calculado

# Chama a função principal para iniciar o programa
Menu()
