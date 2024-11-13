import funcoes, os, time

# Lista para armazenar os números
numeros = []
while True:
    # Limpa a tela
    os.system('cls')
    
    # Opções do menu
    options = [
        '1. Adicionar números à lista',
        '2. Mostrar os elementos com o primeiro e último trocados',
        '3. Sair'
    ]

    # Exibe as opções do menu
    for option in options:
        funcoes.Digitar(option)
    funcoes.Digitar('Escolha uma opção:')
    
    try:
        # Captura a escolha do usuário
        choice = int(input('> '))
        os.system('cls')
    except ValueError:
        # Trata entradas inválidas
        funcoes.Digitar('Digite uma opção válida!')
        time.sleep(1)
        continue

    if choice == 1:
        os.system('cls')
        try:
            # Solicita a quantidade de números a serem adicionados
            funcoes.Digitar('Digite a quantidade de números (mínimo: 2):')
            quantidade = int(input("> "))
            if quantidade < 2:
                print("É necessário informar pelo menos dois números para trocar.")
            else:
                # Adiciona números à lista
                for i in range(quantidade):
                    numero = float(input(f"Digite o número {i + 1}: "))
                    numeros.append(numero)
                funcoes.Digitar('Números adicionados com sucesso!')
        except (ValueError, TypeError):
            # Trata entradas inválidas
            funcoes.Digitar('Digite um item válido!')

    elif choice == 2:
        os.system('cls')
        # Verifica se há pelo menos dois números na lista para trocar
        if len(numeros) < 2:
            funcoes.Digitar('A lista deve conter pelo menos dois números para trocar.')
        else:
            # Troca o primeiro e o último número da lista
            numeros[0], numeros[-1] = numeros[-1], numeros[0]
            print("Lista após a troca:", numeros)
        try:
            choice = int(input('Digite 0 para voltar: '))
        except ValueError:
            funcoes.Digitar('Pressione 0 para retornar!')

    elif choice == 3:
        # Finaliza o programa
        funcoes.Digitar('Finalizando...')
        funcoes.Digitar('...')
        break
