import time  # Importa a biblioteca time para controlar o tempo de atraso nas mensagens

# Dicionário para armazenar os dados dos alunos
turma = {}

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

def adicionar_aluno():
    """
    Adiciona um novo aluno ao dicionário 'turma' e solicita suas notas.

    O usuário deve inserir o nome do aluno e três notas, que são validadas para 
    garantir que estejam entre 0 e 10.
    """
    nome = input("Digite o nome do aluno: ")  # Solicita o nome do aluno
    
    notas = []  # Lista para armazenar as notas do aluno
    for i in range(1, 4):  # Loop para solicitar 3 notas
        while True:  # Loop até que uma nota válida seja inserida
            try:
                nota = float(input(f"Digite a nota da disciplina {i}: "))  # Solicita a nota
                if 0 <= nota <= 10:  # Valida se a nota está entre 0 e 10
                    notas.append(nota)  # Adiciona a nota à lista
                    break  # Sai do loop se a nota for válida
                else:
                    digitar("Nota deve ser entre 0 e 10. Tente novamente.")  # Mensagem de erro
            except ValueError:
                digitar("Entrada inválida. Digite um número.")  # Mensagem de erro para entrada não numérica

    turma[nome] = notas  # Adiciona o aluno e suas notas ao dicionário
    digitar(f"Aluno '{nome}' adicionado com sucesso!")  # Mensagem de confirmação

def calcular_media(notas):
    """
    Calcula a média das notas fornecidas.

    Args:
        notas (list): Lista de notas a serem avaliadas.

    Returns:
        float: A média das notas.
    """
    return sum(notas) / len(notas)  # Retorna a soma das notas dividida pelo número de notas

def mostrar_alunos():
    """
    Exibe todos os alunos cadastrados e suas respectivas médias.

    Caso não haja alunos cadastrados, uma mensagem é exibida informando que a turma está vazia.
    """
    if not turma:  # Verifica se o dicionário de alunos está vazio
        digitar("Nenhum aluno cadastrado.")  # Mensagem se não houver alunos
    else:
        digitar("\nAlunos e suas médias:")  # Cabeçalho da lista de alunos
        for nome, notas in turma.items():  # Itera sobre cada aluno e suas notas
            media = calcular_media(notas)  # Calcula a média do aluno
            status = "Aprovado" if media >= 7 else "Reprovado"  # Define o status do aluno
            # Exibe o nome, notas, média e status do aluno
            digitar(f"Nome: {nome}, Notas: {notas}, Média: {media:.2f} - {status}")
        digitar("-" * 30)  # Linha separadora

def menu():
    """
    Exibe um menu de opções para o usuário interagir com o sistema.

    Permite adicionar alunos, mostrar alunos e suas médias ou sair do programa.
    O menu continuará a ser exibido até que o usuário escolha sair.
    """
    while True:
        digitar("Menu:")  # Exibe o cabeçalho do menu
        digitar("1. Adicionar aluno")  # Opção para adicionar aluno
        digitar("2. Mostrar alunos e suas médias")  # Opção para mostrar alunos
        digitar("3. Sair")  # Opção para sair do programa
        
        opcao = input("Escolha uma opção: ")  # Solicita a escolha do usuário

        if opcao == '1':
            adicionar_aluno()  # Chama a função para adicionar aluno
        elif opcao == '2':
            mostrar_alunos()  # Chama a função para mostrar alunos
        elif opcao == '3':
            digitar("Saindo do programa...")  # Mensagem de saída
            break  # Sai do loop e termina o menu
        else:
            digitar("Opção inválida! Tente novamente.")  # Mensagem de erro para opção inválida

# Chamar a função menu
menu()  # Inicia o programa chamando a função menu
