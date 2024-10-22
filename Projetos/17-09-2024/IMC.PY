def Menu():
    while True:
        print('-'*50)
        print('Índice de Massa Corporal')
        print('-'*50)
        options = ['[1] Calcular IMC', '[2] Sair']
        for option in options:
            print(option)
        try:
            print('Selecione uma opção:')
            choice = int(input('> '))
        except (ValueError, TypeError):
            print("Opção inválida. Tente novamente.")
            continue
        
        if choice == 1:
            try:
                p = float(input('Digite o peso (kg): '))
                h = float(input('Digite a altura (m): '))
                print('-'*50)
                IMC, grau = I_M_C(p, h)
                print(f'O IMC é: {IMC:.2f}')
                print(f'Grau IMC: {grau}')
                print('-'*50)
            except (ValueError, TypeError):
                print("Entrada inválida. Tente novamente.")
                continue
        elif choice == 2:
            break
        else:
            print("Opção inválida. Tente novamente.")

def I_M_C(peso, altura):
    baixo_peso = 'Baixo peso'
    peso_normal = 'Peso normal'
    sobrepeso = 'Sobrepeso'
    obesidade_1 = 'Obesidade grau 1'
    obesidade_2 = 'Obesidade grau 2'
    total = peso / (altura ** 2)
    
    if total < 18.5:
        grau = baixo_peso
    elif 18.5 <= total < 25:
        grau = peso_normal
    elif 25 <= total < 30:
        grau = sobrepeso
    elif 30 <= total < 40:
        grau = obesidade_1
    else:
        grau = obesidade_2
    
    return total, grau

Menu()