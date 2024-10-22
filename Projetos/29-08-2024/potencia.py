while True:

    opções = ['[1]Calcular potencia', '[2]Sair']
    print('-'*30)

    for opção in opções:
        print(opção)

    print('-'*30)
    choice = int(input('digite a opção: '))

    if choice == 1:

        print('-'*30)
        base = float(input('digite a Base da potencia: '))

        print('-'*30)

        expoente = int(input('digite o expoente da potencia: '))
        print('-'*30)
        resultado = 1

        for i in range(1, expoente + 1):
            resultado *= base

        print('-'*30)
        print(resultado)
        print('-'*30)
        
    else:
        break