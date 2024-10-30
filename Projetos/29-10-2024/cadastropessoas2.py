import time  # Importa a biblioteca time para controlar o tempo de atraso nas mensagens

# Dicionário para armazenar contatos
contatos = {}

def digitar(texto, atraso=0.03):
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

def adicionar_contato():
    """
    Adiciona um novo contato ao dicionário 'contatos'.

    Solicita o nome e telefone do contato. Se o contato já existir, uma mensagem de
    erro é exibida; caso contrário, o contato é adicionado com sucesso.
    """
    nome = input("Digite o nome do contato: ")  # Solicita o nome do contato
    telefone = input("Digite o telefone do contato: ")  # Solicita o telefone do contato
    
    if nome in contatos:  # Verifica se o contato já existe
        digitar(f"O contato '{nome}' já existe.")  # Mensagem de erro
    else:
        contatos[nome] = telefone  # Adiciona o contato ao dicionário
        digitar(f"Contato '{nome}' adicionado com sucesso!")  # Mensagem de confirmação

def remover_contato():
    """
    Remove um contato do dicionário 'contatos'.

    Solicita o nome do contato a ser removido. Se o contato existir, ele é removido
    com sucesso; caso contrário, uma mensagem de erro é exibida.
    """
    nome = input("Digite o nome do contato que deseja remover: ")  # Solicita o nome do contato
    
    if nome in contatos:  # Verifica se o contato existe
        del contatos[nome]  # Remove o contato do dicionário
        digitar(f"Contato '{nome}' removido com sucesso!")  # Mensagem de confirmação
    else:
        digitar(f"Contato '{nome}' não encontrado.")  # Mensagem de erro

def buscar_contato():
    """
    Busca um contato pelo nome no dicionário 'contatos'.

    Solicita o nome do contato a ser buscado. Se o contato for encontrado, exibe o
    nome e telefone; caso contrário, uma mensagem de erro é exibida.
    """
    nome = input("Digite o nome do contato que deseja buscar: ")  # Solicita o nome do contato
    
    if nome in contatos:  # Verifica se o contato existe
        digitar(f"Contato encontrado: {nome} - Telefone: {contatos[nome]}")  # Exibe o contato
    else:
        digitar(f"Contato '{nome}' não encontrado.")  # Mensagem de erro

def mostrar_contatos():
    """
    Exibe todos os contatos cadastrados.

    Se não houver contatos cadastrados, uma mensagem informando que não há contatos é exibida.
    """
    if not contatos:  # Verifica se o dicionário de contatos está vazio
        digitar("Nenhum contato cadastrado.")  # Mensagem se não houver contatos
    else:
        digitar("\nContatos Cadastrados:")  # Cabeçalho da lista de contatos
        for nome, telefone in contatos.items():  # Itera sobre cada contato
            digitar(f"Nome: {nome}, Telefone: {telefone}")  # Exibe o contato
        digitar("-" * 30)  # Linha separadora

def menu():
    """
    Exibe um menu de opções para o usuário interagir com o sistema de contatos.

    Permite adicionar, remover, buscar contatos, mostrar todos os contatos ou sair do programa.
    O menu continuará a ser exibido até que o usuário escolha sair.
    """
    while True:
        digitar("Menu:")  # Exibe o cabeçalho do menu
        digitar("1. Adicionar contato")  # Opção para adicionar contato
        digitar("2. Remover contato")  # Opção para remover contato
        digitar("3. Buscar contato")  # Opção para buscar contato
        digitar("4. Mostrar todos os contatos")  # Opção para mostrar todos os contatos
        digitar("5. Sair")  # Opção para sair do programa
        
        opcao = input("Escolha uma opção: ")  # Solicita a escolha do usuário

        if opcao == '1':
            adicionar_contato()  # Chama a função para adicionar contato
        elif opcao == '2':
            remover_contato()  # Chama a função para remover contato
        elif opcao == '3':
            buscar_contato()  # Chama a função para buscar contato
        elif opcao == '4':
            mostrar_contatos()  # Chama a função para mostrar contatos
        elif opcao == '5':
            digitar("Saindo do programa...")  # Mensagem de saída
            break  # Sai do loop e termina o menu
        else:
            digitar("Opção inválida! Tente novamente.")  # Mensagem de erro para opção inválida

# Chamar a função menu
menu()  # Inicia o programa chamando a função menu
