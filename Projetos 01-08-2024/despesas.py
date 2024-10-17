import time

time.sleep(2)


class Despesas:
    def __init__(self, descricao, categoria, valor):
        self.descricao = descricao
        self.categoria = categoria
        self.valor = valor



class ControleDespesas:
    def __init__(self):
        self.despesas = []

    def adicionar_despesas(self, despesas):
        self.despesas.append(despesas)

    def listar_despesas(self):
        if self.despesas:
            for index, despesa in enumerate(self.despesas, start=1):
                print("-"*30)
                print(f"{index}. Descrição: {despesa.descricao}")
                print(f"Categoria: {despesa.categoria}")
                print(f"Valor: R${despesa.valor}")
                print("-"*30)

        else:
            print("-"*30)
            print("Nada encontrado!")
            print("-"*30)
            time.sleep(1)

if __name__ == '__main__':
    controle = ControleDespesas()

    while True:
        print('1. Adcionar Despesa.')
        print('2. Listar despesas.')
        print('3. Sair.')
        print("-"*30)
        opcao = input('Escolha uma opção:\n')
        print("-"*30)