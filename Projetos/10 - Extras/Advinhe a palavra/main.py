import time

def Type(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def Word_List():
    question = [
        '',
        '',
        '',
        '',
    ]

def Game():
    while True:
        options = [
            '1. Jogar',
            '2. Sair',
        ]
        Type("Escolha uma opção:")
        for option in options:
            Type(option)
        try:
            choice = int(input('> '))
        except ValueError:
            Type("Digite 1 para jogar ou 2 para sair ve")
            time.sleep(1)
            continue
        if choice == 2:
            Type('Finalizando...')
            break
        if choice == 1:
            Type('Deu certo')
        else:
            Type('Digite 1 para jogar ou 2 para sair')
Game()