def Menu():
    while True:
        print('-'*50)
        print('Area do Retangulo')
        print('-'*50)
        options = ['[1]Calcular area do Retagulo', '[2]Sair']
        for option in options:
            print(option)
        try:
            print('Selecione uma opção:')
            choice = int(input('> '))
        except (ValueError, TypeError) as e:
            continue
        if choice == 1:
            try:
                b = float(input('Digite a base: '))
                h = float(input('Digite a altura: '))
                A = 0
                print('-'*50)
                print(f'A area do retangulo é: {Area_Retangulo(A, b, h)}')
                print('-'*50)
            except (ValueError, TypeError) as e:
                continue
        else:
            break

def Area_Retangulo(Area, base, altura):
    parcial = base * altura
    Area = parcial
    return Area

Menu()