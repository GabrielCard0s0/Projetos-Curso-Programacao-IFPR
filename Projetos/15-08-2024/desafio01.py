import time

saldo = 500.00
senha = 54321
conta = 858585
digito = 8

def Login():
    print('-'*30)
    contausuario = int(input('Digite o numeto da conta: '))
    if contausuario == conta:
        digitousuario = int(input('Digite o digito da conta: '))
        if digitousuario == digito:
            senhausuario =  int(input('Digite a senha: '))
            if senhausuario == senha:
                print('-'*30)
                return MainMenu()
            else:
                print('-'*30)
                print(f'Senha inválida!{senhausuario} Tente novamente.')
                return Login()
        else:
            print('-'*30)
            print(f'Digito inválido! Tente novamente.')
            return Login()
    else:
        print('-'*30)
        print(f'Conta inválida! Tente novamente.')
        return Login()
        

def MainMenu():
    print('-'*30)
    print(f'1. Mostrar saldo\n 2. Fazer um saque\n 3. Fazer um depósito\n 4. Sair')
    print('-'*30)
    choice = int(input('Digite a opção: '))
    if choice == 1:
        time.sleep(1)
        return MostrarSaldo()
    elif choice == 2:
        time.sleep(1)
        return FazerSaque()
    elif choice == 3:
        time.sleep(1)
        return FazerDeposito()
    elif choice == 4:
        time.sleep(1)
        return Sair()
    else:
        print('-'*30)
        print(f'Opção inválida! Tente novamente.')
        time.sleep(1)
        return MainMenu()

def MostrarSaldo():
    print('-'*30)
    print(f'Seu saldo atual é', 'R$', {saldo})
    print('-'*30)
    time.sleep(2)
    return MainMenu()

def FazerSaque():
    global saldo
    print('-'*30)
    print('Saldo atual: ', 'R$', saldo)
    saque = float(input('Digite o valor que deseja sacar: '))
    print('-'*30)
    if saque <= saldo:
        saldo = saldo - saque
        print('Saque realizado com sucesso!', '\nSeu novo saldo é: ', 'R$', saldo)
        time.sleep(1)
        return MainMenu()
    else:
        print('-'*30)
        print(f'Saldo insuficiente! Digite um saldo válido.')
        time.sleep(1)
        return FazerSaque()

def FazerDeposito():
    global saldo
    print('-'*30)
    print(f'Saldo atual: ', 'R$', {saldo}, )
    deposito = float(input('Digite o valor que deseja depositar: '))
    print('-'*30)
    saldo = saldo + deposito
    print(f'Saque realizado com sucesso!', '\nSeu novo saldo é: ', 'R$', {saldo})
    time.sleep(1)
    return MainMenu()

def Sair():
    print('-'*30)
    print(f'Finalizando...')
    print('-'*30)


print('-'*30)
print(f'Bem-vindo ao Banco Saque-Sorridente')
print('-'*30)

time.sleep(1)


Login()