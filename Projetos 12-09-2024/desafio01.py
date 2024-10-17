
class Menu:
    def __init__(self):
        self.options = ['[1]Somar algarismos', '[2]Sair']

    def Main(self):
        while True:
            print('Selecione uma opção:')
            for option in self.options:
                print(option)
            try:
                choice = int(input('> '))
                if choice == 1:
                    self.Somar_Algarismos()
                elif choice == 2:
                    break
            except (ValueError, TypeError)as e:
                print('Opção inválida. Tente Novamente.')

    def Somar_Algarismos(self):
        numero = int(input("Digite um número inteiro: "))

        resultado = 0
        while numero != 0:
                
            digito = numero % 10
                
            resultado += digito
                
            numero //= 10

        print(f"A soma dos algarismos é: {resultado}")


menu = Menu()
menu.Main()