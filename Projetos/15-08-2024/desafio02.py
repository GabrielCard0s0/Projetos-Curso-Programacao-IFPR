import time

def MainMenu():
    print('-' * 30)
    print(f'1. Inserir salário.\n2. Sair')
    print('-' * 30)
    choice = int(input('Digite a opção: '))
    
    if choice == 1:
        salario = float(input('Digite o Salário: '))
        desconto_inss = 0
        
        # Cálculo do INSS
        if salario < 1412.00:
            desconto_inss = salario * 0.075
        elif 1412.00 <= salario < 2666.68:
            desconto_inss = (1412.00 * 0.075) + ((salario - 1412.00) * 0.09)
        elif 2666.69 <= salario < 4000.03:
            desconto_inss = 105.90 + 207.91 + ((salario - 2666.69) * 0.12)
        elif 4000.03 <= salario <= 7786.02:
            desconto_inss = 105.90 + 207.91 + 354.07 + ((salario - 3751.06) * 0.14)
        else:  # salario > 7786.02
            desconto_inss = 105.90 + 207.91 + 354.07 + 205.57 + (salario * 0.275)
        
        salario_liquido = salario - desconto_inss

        # Cálculo do IRPF
        if salario_liquido >= 2826.66:
            if salario_liquido < 3751.05:
                desconto_irpf = 69.33 + (salario_liquido * 0.15)
            else:
                desconto_irpf = 69.33 + 138.65 + (salario_liquido * 0.225)
            salario_liquido -= desconto_irpf
        
        print('-' * 30)
        print(f'Salário Líquido: {salario_liquido:.2f}')
        print('-' * 30)
        time.sleep(1)
        return MainMenu()

    elif choice == 2:
        print('-' * 30)
        print(f'Finalizando...')
        print('-' * 30)
    else:
        print('-' * 30)
        print(f'Opção inválida! Tente novamente.')
        print('-' * 30)
        time.sleep(1)
        return MainMenu()

# Início do programa
MainMenu()
