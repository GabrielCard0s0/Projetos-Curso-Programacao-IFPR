import time

# Inicializa as variáveis de saldo, senha, conta e dígito
saldo = 500.00
senha = 54321
conta = 858585
digito = 8

def Login():
    # Função para realizar o login do usuário
    print('-' * 30)
    contausuario = int(input('Digite o número da conta: '))  # Solicita o número da conta
    if contausuario == conta:  # Verifica se a conta está correta
        digitousuario = int(input('Digite o dígito da conta: '))  # Solicita o dígito da conta
        if digitousuario == digito:  # Verifica se o dígito está correto
            senhausuario = int(input('Digite a senha: '))  # Solicita a senha
            if senhausuario == senha:  # Verifica se a senha está correta
                print('-' * 30)
                return MainMenu()  # Chama o menu principal
            else:
                print('-' * 30)
                print(f'Senha inválida! {senhausuario}. Tente novamente.')
                return Login()  # Repetir login em caso de senha inválida
        else:
            print('-' * 30)
            print(f'Dígito inválido! Tente novamente.')
            return Login()  # Repetir login em caso de dígito inválido
    else:
        print('-' * 30)
        print(f'Conta inválida! Tente novamente.')
        return Login()  # Repetir login em caso de conta inválida


def MainMenu():
    # Função para exibir o menu principal
    print('-' * 30)
    print(f'1. Mostrar saldo\n2. Fazer um saque\n3. Fazer um depósito\n4. Sair')
    print('-' * 30)
    choice = int(input('Digite a opção: '))  # Solicita a escolha do usuário
    if choice == 1:
        time.sleep(1)
        return MostrarSaldo()  # Chama a função para mostrar o saldo
    elif choice == 2:
        time.sleep(1)
        return FazerSaque()  # Chama a função para fazer um saque
    elif choice == 3:
        time.sleep(1)
        return FazerDeposito()  # Chama a função para fazer um depósito
    elif choice == 4:
        time.sleep(1)
        return Sair()  # Chama a função para sair
    else:
        print('-' * 30)
        print(f'Opção inválida! Tente novamente.')
        time.sleep(1)
        return MainMenu()  # Repetir menu em caso de opção inválida

def MostrarSaldo():
    # Função para mostrar o saldo atual
    print('-' * 30)
    print(f'Seu saldo atual é: R$ {saldo}')  # Exibe o saldo
    print('-' * 30)
    time.sleep(2)
    return MainMenu()  # Retorna ao menu principal

def FazerSaque():
    # Função para realizar um saque
    global saldo
    print('-' * 30)
    print('Saldo atual: R$', saldo)  # Exibe o saldo atual
    saque = float(input('Digite o valor que deseja sacar: '))  # Solicita o valor do saque
    print('-' * 30)
    if saque <= saldo:  # Verifica se há saldo suficiente
        saldo -= saque  # Deduz o valor do saque do saldo
        print('Saque realizado com sucesso!', '\nSeu novo saldo é: R$', saldo)
        time.sleep(1)
        return MainMenu()  # Retorna ao menu principal
    else:
        print('-' * 30)
        print(f'Saldo insuficiente! Digite um valor válido.')
        time.sleep(1)
        return FazerSaque()  # Repetir saque em caso de saldo insuficiente

def FazerDeposito():
    # Função para realizar um depósito
    global saldo
    print('-' * 30)
    print(f'Saldo atual: R$', saldo)  # Exibe o saldo atual
    deposito = float(input('Digite o valor que deseja depositar: '))  # Solicita o valor do depósito
    print('-' * 30)
    saldo += deposito  # Adiciona o valor do depósito ao saldo
    print('Depósito realizado com sucesso!', '\nSeu novo saldo é: R$', saldo)
    time.sleep(1)
    return MainMenu()  # Retorna ao menu principal

def Sair():
    # Função para encerrar o programa
    print('-' * 30)
    print(f'Finalizando...')
    print('-' * 30)

# Início do programa
print('-' * 30)
print(f'Bem-vindo ao Banco Saque-Sorridente')
print('-' * 30)
time.sleep(1)

Login()  # Inicia o processo de login
