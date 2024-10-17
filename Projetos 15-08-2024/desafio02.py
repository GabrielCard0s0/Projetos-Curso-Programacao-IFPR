import time

def MainMenu():
    print('-'*30)
    print(f'1. Inserir salário. \n2. Sair')
    print('-'*30)
    choice = int(input('Digite a opção: '))
    if choice == 1:
        salario = float(input('Digite o Salário: '))
        if salario < 1412.00:
            desconto_inss = salario * 0.075
            salario_liquido = salario - desconto_inss
            print('-'*30)
            print(f'Salário Líquido: {salario_liquido:.2f}')
            print('-'*30)
            time.sleep(1)
            return MainMenu()
        elif 1412.00 <= salario < 2666.68:
            desconto_inss = (1412.00 * 0.075) + ((salario - 1412.00) * 0.09)
            salario_liquido = salario - desconto_inss
            if 2259.21 <= salario_liquido < 2826.65:
                desconto_irpf = salario_liquido * 0.075
                salario_liquido -= desconto_irpf
                print('-'*30)
                print(f'Salário Líquido: {salario_liquido:.2f}')
                print('-'*30)
                time.sleep(1)
                return MainMenu()
            else:
                print('-'*30)
                print(f'Salário Líquido: {salario_liquido:.2f}')
                print('-'*30)
                time.sleep(1)
                return MainMenu()
        elif 2666.69 <= salario < 4000.03:
            desconto_inss = 105.90 + 207.91 + ((salario - 2666.69) * 0.12)
            salario_liquido = salario - desconto_inss
            if 2826.66 <= salario_liquido < 3751.05:
                desconto_irpf = 69.33 + (salario_liquido * 0.15)
                salario_liquido -= desconto_irpf
                print('-'*30)
                print(f'Salário Líquido: {salario_liquido:.2f}')
                print('-'*30)  
                time.sleep(1)
                return MainMenu() 
            else:
                print(f'Salário Líquido: {salario_liquido:.2f}')
                time.sleep(1)
                return MainMenu()   
        elif salario >= 3751.06 <= 7786.02:
            desconto_inss = 105.90 + 207.91 + 354.07 + ((salario - 3751.06) * 0.14)
            salario_liquido = salario - desconto_inss
            if salario_liquido >= 3751.05 <= 4664.68:
                desconto_irpf = 69.33 + 138.65 + (salario_liquido * 0.225)
                salario_liquido -= desconto_irpf
                print('-'*30)
                print(f'Salário Líquido: {salario_liquido:.2f}')
                print('-'*30)
                time.sleep(1)
                return MainMenu()
            else:
                print('-'*30)
                print(f'Salário Líquido: {salario_liquido:.2f}')
                print('-'*30)
                time.sleep(1)
                return MainMenu()
        elif salario > 4664.68:
            print('-'*30)
            desconto_inss = 105.90 + 207.91 + 354.07 + 205.57 + (salario * 0.275)
            salario_liquido -= desconto_inss
            print(f'Salário Líquido: {salario_liquido:.2f}')
            print('-'*30)
            time.sleep(1)
            return MainMenu()
        else:
            print('-'*30)
            print(f'Opção inválida! Tente novamente.')
            print('-'*30)
            time.sleep(1)
            return MainMenu()
    elif choice == 2:
        print('-'*30)
        print(f'Finalizando...')
        print('-'*30)
    else:
        print('-'*30)
        print(f'Opção inválida! Tente novamente.')
        print('-'*30)
        time.sleep(1)
        return MainMenu()

MainMenu()