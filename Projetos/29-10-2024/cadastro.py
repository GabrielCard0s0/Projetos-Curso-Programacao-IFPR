import time

# Lista para armazenar os dados das pessoas
pessoas_cadastradas = []

def cadastrar_pessoa():# Solicitar os dados da pessoa
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o e-mail: ")

    # Criar um dicionário com os dados da pessoa
    pessoa = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone,
        "email": email
    }

    # Adicionar a pessoa à lista
    pessoas_cadastradas.append(pessoa)

    # Mostrar os dados cadastrados
    Digitar("\nDados Cadastrados:")
    Digitar(f"Nome: {nome}")
    Digitar(f"Idade: {idade}")
    Digitar(f"Telefone: {telefone}")
    Digitar(f"E-mail: {email}")
    Digitar("-" * 30)

def mostrar_pessoas():
    if not pessoas_cadastradas:
        Digitar("Nenhuma pessoa cadastrada.")
    else:
        Digitar("\nPessoas Cadastradas:")
        for pessoa in pessoas_cadastradas:
            Digitar(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Telefone: {pessoa['telefone']}, E-mail: {pessoa['email']}")
        Digitar("-" * 30)

def Digitar(texto, atraso=0.02):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(atraso)
    print()

def menu():
    while True:
        Digitar("Menu:")
        Digitar("1. Cadastrar pessoa")
        Digitar("2. Mostrar pessoas cadastradas")
        Digitar("3. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_pessoa()
        elif opcao == '2':
            mostrar_pessoas()
        elif opcao == '3':
            Digitar("Saindo do programa...")
            break
        else:
            Digitar("Opção inválida! Tente novamente.")

# Chamar a função menu
menu()
