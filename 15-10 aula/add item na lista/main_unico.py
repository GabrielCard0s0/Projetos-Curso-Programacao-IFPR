import os, time

def Digitar(texto, atraso=0.02):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(atraso)
    print('\n')

lista = []
while True:
    os.system('cls')
    options = [
        '1. Adicionar item a lista',
        '2. Mostrar a quantidade de elementos na lista',
        '3. Sair'
    ]
    for option in options:
        Digitar(option)
    Digitar('Escolha uma opção:')
    try:
        choice = int(input('> '))
        os.system('cls')
    except ValueError:
        Digitar('Digite uma opção válida!')
        time.sleep(1)
    if choice == 1:
        os.system('cls')
        try:
            Digitar('Digite o item:')
            add = input('> ')
            lista.append(add)
            Digitar('Item adcionado!')
            time.sleep(0.5)
        except (ValueError, TypeError):
            Digitar('Digite uma item válido!')
    if choice == 2:
        os.system('cls')
        print(f'A lista possui {len(lista)} itens.')
        try:
            choice = int(input('digite 0 para voltar: '))
        except ValueError:
            Digitar('Pressione 0 para retornar!')
    if choice == 3:
        Digitar('Finalizando...')
        Digitar('...')
        break