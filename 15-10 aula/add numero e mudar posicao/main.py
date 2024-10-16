import funcoes, os, time

numeros = []
while True:
    os.system('cls')
    options = [
        '1. Adcionar numeros a lista',
        '2. Mostrar os elementos com primeiro e ultimo trocados',
        '3. Sair'
    ]

    for option in options:
        funcoes.Digitar(option)
    funcoes.Digitar('Escolha uma opção:')
    try:
        choice = int(input('> '))
        os.system('cls')
    except ValueError:
        funcoes.Digitar('Digite uma opção válida!')
        time.sleep(1)
        continue

    if choice == 1:
        os.system('cls')
        try:
            funcoes.Digitar('Digite a quantidade de números(min: 2):')
            quantidade = int(input("> "))
            if quantidade < 2:
                print("É necessário informar pelo menos dois números para trocar.")
            else:
                for i in range(quantidade):
                    numero = float(input(f"Digite o número {i + 1}: "))
                    numeros.append(numero)
        except (ValueError, TypeError):
            funcoes.Digitar('Digite uma item válido!')

    if choice == 2:
        os.system('cls')
        numeros[0], numeros[-1] = numeros[-1], numeros[0]
        print("Lista após a troca:", numeros)
        try:
            choice = int(input('digite 0 para voltar: '))
        except ValueError:
            funcoes.Digitar('Pressione 0 para retornar!')

    if choice == 3:
        funcoes.Digitar('Finalizando...')
        funcoes.Digitar('...')
        break