import funcoes, os, time

def Digitar(texto, atraso=0.02):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(atraso)
    print('\n')

numeros = []
while True:
    os.system('cls')
    options = [
        '1. Adcionar numeros a lista',
        '2. Mostrar os elementos com primeiro e ultimo trocados',
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
        continue

    if choice == 1:
        os.system('cls')
        try:
            Digitar('Digite a quantidade de números(min: 2):')
            quantidade = int(input("> "))
            if quantidade < 2:
                print("É necessário informar pelo menos dois números para trocar.")
            else:
                for i in range(quantidade):
                    numero = float(input(f"Digite o número {i + 1}: "))
                    numeros.append(numero)
        except (ValueError, TypeError):
            Digitar('Digite uma item válido!')

    if choice == 2:
        os.system('cls')
        numeros[0], numeros[-1] = numeros[-1], numeros[0]
        print("Lista após a troca:", numeros)
        try:
            choice = int(input('digite 0 para voltar: '))
        except ValueError:
            Digitar('Pressione 0 para retornar!')

    if choice == 3:
        Digitar('Finalizando...')
        Digitar('...')
        break