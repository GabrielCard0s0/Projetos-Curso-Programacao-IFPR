class Menu:
    def __init__(self):
        # Inicializa as opções do menu
        self.options = ['[1] Somar algarismos', '[2] Sair']

    def Main(self):
        # Método principal que exibe o menu e lida com a entrada do usuário
        while True:
            print('Selecione uma opção:')
            for option in self.options:
                print(option)
            try:
                # Solicita ao usuário que escolha uma opção
                choice = int(input('> '))
                if choice == 1:
                    # Se a escolha for 1, chama o método para somar algarismos
                    self.Somar_Algarismos()
                elif choice == 2:
                    # Se a escolha for 2, sai do loop
                    break
            except (ValueError, TypeError) as e:
                # Trata exceções se a entrada não for válida
                print('Opção inválida. Tente Novamente.')

    def Somar_Algarismos(self):
        # Solicita ao usuário que digite um número inteiro
        numero = int(input("Digite um número inteiro: "))

        resultado = 0
        # Enquanto o número não for 0, continua a somar os algarismos
        while numero != 0:
            digito = numero % 10  # Obtém o último dígito do número
            resultado += digito    # Adiciona o dígito ao resultado
            numero //= 10          # Remove o último dígito do número

        # Exibe o resultado da soma dos algarismos
        print(f"A soma dos algarismos é: {resultado}")


# Cria uma instância do menu e chama o método principal
menu = Menu()
menu.Main()
