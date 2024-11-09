import time  # Importa a biblioteca time para controlar o tempo de atraso nas mensagens

# Lista para armazenar os produtos cadastrados
lista_produtos = []

def Cadastrar_Produto():
    """
    Solicita ao usuário a quantidade de produtos a serem cadastrados e seus dados.

    Os dados solicitados incluem descrição, valor e código de barras.
    Após o cadastro, os produtos são exibidos.
    """
    try:
        Digitar('Quantos produtos vai cadastrar?')  # Solicita a quantidade de produtos
        quantidade = int(input('> '))  # Lê a quantidade de produtos
        
        if quantidade <= 0:  # Verifica se a quantidade é válida
            Digitar("Digite uma quantidade válida!")
        else:
            while quantidade != 0:  # Loop para cadastrar os produtos
                descricao = input(f"Digite o nome do produto: ")  # Solicita a descrição do produto
                valor = input("Digite o valor: ")  # Solicita o valor do produto
                cod = input("Digite o código de barras: ")  # Solicita o código de barras

                # Cria um dicionário com os dados do produto
                produto = {
                    "Descrição": descricao,
                    "Valor": valor,
                    "Código de Barras": cod,
                }
                lista_produtos.append(produto)  # Adiciona o produto à lista
                quantidade -= 1  # Decrementa a quantidade
                print('#' * 50)  # Exibe uma linha separadora
    except ValueError:
        Digitar("Digite uma quantidade válida")  # Mensagem de erro para entrada não numérica
    Mostrar_produtos()  # Chama a função para mostrar os produtos cadastrados

def Mostrar_produtos():
    """
    Exibe todos os produtos cadastrados na lista 'lista_produtos'.

    Se não houver produtos cadastrados, uma mensagem é exibida informando que a lista está vazia.
    """
    if not lista_produtos:  # Verifica se a lista está vazia
        Digitar("Nenhum produto cadastrado.")  # Mensagem se não houver produtos
    else:
        Digitar("\nProdutos Cadastrados:")  # Cabeçalho da lista de produtos
        for produto in lista_produtos:  # Itera sobre cada produto na lista
            # Exibe os dados do produto
            Digitar(f"Descrição: {produto['Descrição']}, Valor: {produto['Valor']}, Código de Barras: {produto['Código de Barras']}")
        Digitar("-" * 30)  # Linha separadora

def Digitar(texto, atraso=0.03):
    """
    Simula a digitação de um texto na tela com um atraso entre as letras.

    Args:
        texto (str): O texto a ser exibido.
        atraso (float): O tempo de espera entre a impressão de cada letra (padrão é 0.03 segundos).
    """
    for letra in texto:  # Itera sobre cada letra do texto
        print(letra, end='', flush=True)  # Imprime a letra sem quebrar a linha
        time.sleep(atraso)  # Espera um tempo definido antes de imprimir a próxima letra
    print()  # Adiciona uma nova linha ao final

def menu():
    """
    Exibe um menu de opções para o usuário interagir com o sistema de cadastro de produtos.

    Permite cadastrar produtos, mostrar produtos cadastrados ou sair do programa.
    O menu continuará a ser exibido até que o usuário escolha sair.
    """
    while True:
        Digitar("Menu:")  # Exibe o cabeçalho do menu
        Digitar("1. Cadastrar produtos")  # Opção para cadastrar produtos
        Digitar("2. Mostrar produtos cadastrados")  # Opção para mostrar produtos cadastrados
        Digitar("3. Sair")  # Opção para sair do programa
        
        opcao = input("Escolha uma opção: ")  # Solicita a escolha do usuário

        if opcao == '1':
            Cadastrar_Produto()  # Chama a função para cadastrar produtos
        elif opcao == '2':
            Mostrar_produtos()  # Chama a função para mostrar produtos cadastrados
        elif opcao == '3':
            Digitar("Saindo do programa...")  # Mensagem de saída
            break  # Sai do loop e termina o menu
        else:
            Digitar("Opção inválida! Tente novamente.")  # Mensagem de erro para opção inválida

# Chama a função menu
menu()  # Inicia o programa chamando a função menu
