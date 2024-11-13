import time  # Importa a biblioteca time para controlar o tempo de atraso nas mensagens

# Lista para armazenar os dados das pessoas
pessoas_cadastradas = []

def cadastrar_pessoa():
    """
    Solicita os dados de uma pessoa e a cadastra na lista 'pessoas_cadastradas'.

    Os dados solicitados incluem nome, idade, telefone e e-mail.
    Após o cadastro, os dados da pessoa são exibidos.
    """
    nome = input("Digite o nome: ")  # Solicita o nome da pessoa
    idade = input("Digite a idade: ")  # Solicita a idade da pessoa
    telefone = input("Digite o telefone: ")  # Solicita o telefone da pessoa
    email = input("Digite o e-mail: ")  # Solicita o e-mail da pessoa

    # Criar um dicionário com os dados da pessoa
    pessoa = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone,
        "email": email
    }

    # Adicionar a pessoa à lista
    pessoas_cadastradas.append(pessoa)  # Adiciona o dicionário à lista de pessoas cadastradas

    # Mostrar os dados cadastrados
    Digitar("\nDados Cadastrados:")  # Exibe cabeçalho
    Digitar(f"Nome: {nome}")  # Exibe o nome
    Digitar(f"Idade: {idade}")  # Exibe a idade
    Digitar(f"Telefone: {telefone}")  # Exibe o telefone
    Digitar(f"E-mail: {email}")  # Exibe o e-mail
    Digitar("-" * 30)  # Linha separadora

def mostrar_pessoas():
    """
    Exibe todas as pessoas cadastradas na lista 'pessoas_cadastradas'.

    Se não houver pessoas cadastradas, uma mensagem é exibida informando que a lista está vazia.
    """
    if not pessoas_cadastradas:  # Verifica se a lista está vazia
        Digitar("Nenhuma pessoa cadastrada.")  # Mensagem se não houver pessoas
    else:
        Digitar("\nPessoas Cadastradas:")  # Cabeçalho da lista de pessoas
        for pessoa in pessoas_cadastradas:  # Itera sobre cada pessoa na lista
            # Exibe os dados da pessoa
            Digitar(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Telefone: {pessoa['telefone']}, E-mail: {pessoa['email']}")
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
    Exibe um menu de opções para o usuário interagir com o sistema de cadastro.

    Permite cadastrar pessoas, mostrar pessoas cadastradas ou sair do programa.
    O menu continuará a ser exibido até que o usuário escolha sair.
    """
    while True:
        Digitar("Menu:")  # Exibe o cabeçalho do menu
        Digitar("1. Cadastrar pessoa")  # Opção para cadastrar pessoa
        Digitar("2. Mostrar pessoas cadastradas")  # Opção para mostrar pessoas cadastradas
        Digitar("3. Sair")  # Opção para sair do programa
        
        opcao = input("Escolha uma opção: ")  # Solicita a escolha do usuário

        if opcao == '1':
            cadastrar_pessoa()  # Chama a função para cadastrar pessoa
        elif opcao == '2':
            mostrar_pessoas()  # Chama a função para mostrar pessoas cadastradas
        elif opcao == '3':
            Digitar("Saindo do programa...")  # Mensagem de saída
            break  # Sai do loop e termina o menu
        else:
            Digitar("Opção inválida! Tente novamente.")  # Mensagem de erro para opção inválida

# Chamar a função menu
menu()  # Inicia o programa chamando a função menu