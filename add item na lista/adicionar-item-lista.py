import funcoes, os, time

lista = []
while True:
    os.system('cls')
    options = [
        '1. Adicionar item a lista',
        '2. Mostrar a quantidade de elementos na lista',
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
    if choice == 1:
        os.system('cls')
        try:
            funcoes.Digitar('Digite o item:')
            add = input('> ')
            lista.append(add)
            funcoes.Digitar('Item adcionado!')
            time.sleep(0.5)
        except (ValueError, TypeError):
            funcoes.Digitar('Digite uma item válido!')
    if choice == 2:
        os.system('cls')
        print(f'A lista possui {len(lista)} itens.')
        try:
            choice = int(input('digite 0 para voltar: '))
        except ValueError:
            funcoes.Digitar('Pressione 0 para retornar!')
    if choice == 3:
        funcoes.Digitar('Finalizando...')
        funcoes.Digitar('...')
        break