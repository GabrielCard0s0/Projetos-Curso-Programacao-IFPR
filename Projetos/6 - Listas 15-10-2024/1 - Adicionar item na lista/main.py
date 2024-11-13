import funcoes
import os
import time

lista = []
while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela de forma compatível com diferentes sistemas
    options = [
        '1. Adicionar item à lista',
        '2. Mostrar a quantidade de elementos na lista',
        '3. Sair'
    ]
    
    for option in options:
        funcoes.Digitar(option)
    
    funcoes.Digitar('Escolha uma opção:')
    
    try:
        choice = int(input('> '))
        os.system('cls' if os.name == 'nt' else 'clear')
    except ValueError:
        funcoes.Digitar('Digite uma opção válida!')
        time.sleep(1)
        continue  # Volta para o início do loop

    if choice == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        funcoes.Digitar('Digite o item:')
        add = input('> ')
        lista.append(add)
        funcoes.Digitar('Item adicionado!')
        time.sleep(0.5)

    elif choice == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        funcoes.Digitar(f'A lista possui {len(lista)} itens.')
        input('Pressione Enter para voltar...')  # Espera o usuário pressionar Enter para voltar

    elif choice == 3:
        funcoes.Digitar('Finalizando...')
        funcoes.Digitar('...')
        break
    
    else:
        funcoes.Digitar('Opção inválida! Tente novamente.')
