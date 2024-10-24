import time  # Importa a biblioteca time para usar o atraso

# Pausa a execução por 2 segundos
time.sleep(2)

# Classe que representa uma despesa
class Despesas:
    def __init__(self, descricao, categoria, valor):
        self.descricao = descricao  # Atributo para a descrição da despesa
        self.categoria = categoria    # Atributo para a categoria da despesa
        self.valor = valor            # Atributo para o valor da despesa

# Classe para controlar as despesas
class ControleDespesas:
    def __init__(self):
        self.despesas = []  # Inicializa uma lista vazia para armazenar as despesas

    # Método para adicionar uma despesa à lista
    def adicionar_despesas(self, despesas):
        self.despesas.append(despesas)

    # Método para listar todas as despesas
    def listar_despesas(self):
        if self.despesas:  # Verifica se há despesas na lista
            for index, despesa in enumerate(self.despesas, start=1):
                print("-"*30)
                print(f"{index}. Descrição: {despesa.descricao}")  # Imprime a descrição da despesa
                print(f"Categoria: {despesa.categoria}")  # Imprime a categoria da despesa
                print(f"Valor: R${despesa.valor}")  # Imprime o valor da despesa
                print("-"*30)
        else:
            # Se não houver despesas, informa ao usuário
            print("-"*30)
            print("Nada encontrado!")
            print("-"*30)
            time.sleep(1)  # Aguarda 1 segundo antes de continuar

# Inicia o programa principal
if __name__ == '__main__':
    controle = ControleDespesas()  # Cria uma instância da classe ControleDespesas

    while True:
        # Exibe o menu de opções para o usuário
        print('1. Adicionar Despesa.')
        print('2. Listar despesas.')
        print('3. Sair.')
        print("-"*30)
        
        # Solicita que o usuário escolha uma opção
        opcao = input('Escolha uma opção:\n')
        print("-"*30)
