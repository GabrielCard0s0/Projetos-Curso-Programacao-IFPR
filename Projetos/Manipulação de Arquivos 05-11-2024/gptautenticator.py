import time
from getpass import getpass  # Para ocultar a senha durante a digitação

def type_text(text, delay=0.05):
    """
    Digita o texto letra por letra com um atraso entre cada letra.
    
    Parâmetros:
    text (str): O texto a ser digitado.
    delay (float): O atraso em segundos entre cada letra (padrão é 0.05).
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def save_credentials(username, password, file_path="credentials.txt"):
    """
    Salva as credenciais do usuário no arquivo.
    
    Parâmetros:
    username (str): Nome de usuário
    password (str): Senha do usuário
    file_path (str): Caminho do arquivo (padrão: credentials.txt)
    """
    try:
        with open(file_path, 'w') as file:
            # Salvando no formato "username:password"
            file.write(f"{username}:{password}")
        type_text("Credenciais salvas com sucesso!")
    except Exception as e:
        type_text(f"Erro ao salvar credenciais: {e}")

def verify_credentials(username, password, file_path="credentials.txt"):
    """
    Verifica se as credenciais fornecidas correspondem às salvas.
    
    Parâmetros:
    username (str): Nome de usuário fornecido
    password (str): Senha fornecida
    file_path (str): Caminho do arquivo (padrão: credentials.txt)
    
    Retorna:
    bool: True se as credenciais estiverem corretas, False caso contrário
    """
    try:
        with open(file_path, 'r') as file:
            stored_credentials = file.read().strip()
            stored_username, stored_password = stored_credentials.split(':')
            return username == stored_username and password == stored_password
    except Exception as e:
        type_text(f"Erro ao verificar credenciais: {e}")
        return False

def login():
    """
    Realiza o processo de login.
    """
    type_text("\nLOGIN")
    type_text("=" * 20)
    username = input("Nome de usuário: ")
    password = getpass("Senha: ")  # getpass oculta a senha durante a digitação
    
    if verify_credentials(username, password):
        type_text("\nLogin realizado com sucesso!")
        return True
    else:
        type_text("\nCredenciais inválidas!")
        return False

def register():
    """
    Realiza o processo de registro de novo usuário.
    """
    type_text("\nREGISTRO DE NOVO USUÁRIO")
    type_text("=" * 30)
    
    username = input("Escolha um nome de usuário: ")
    while True:
        password = getpass("Escolha uma senha: ")
        confirm_password = getpass("Confirme a senha: ")
        
        if password == confirm_password:
            save_credentials(username, password)
            type_text("\nUsuário registrado com sucesso!")
            break
        else:
            type_text("\nAs senhas não correspondem. Tente novamente.")

def show_credentials():
    """
    Mostra as credenciais armazenadas (apenas para fins de demonstração).
    """
    try:
        with open("credentials.txt", 'r') as file:
            content = file.read()
            username = content.split(':')[0]
            type_text(f"\nUsuário registrado: {username}")
            type_text("(Senha oculta por segurança)")
    except Exception as e:
        type_text("Nenhum usuário registrado ainda.")

def menu():
    """
    Exibe o menu principal com todas as opções disponíveis.
    """
    while True:
        type_text("\nSistema de Autenticação")
        type_text("=" * 40)
        type_text("1. Registrar novo usuário")
        type_text("2. Fazer login")
        type_text("3. Mostrar usuário registrado")
        type_text("4. Sair")
        type_text("=" * 40)
        
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == '1':
            register()
        elif opcao == '2':
            if login():
                while True:
                    type_text("\nÁrea Logada")
                    type_text("=" * 40)
                    type_text("1. Sair da conta")
                    type_text("=" * 40)
                    
                    escolha = input("Escolha uma opção (1): ")
                    if escolha == '1':
                        type_text("\nDeslogando...")
                        break
                    else:
                        type_text("\nOpção inválida!")
        elif opcao == '3':
            show_credentials()
        elif opcao == '4':
            type_text("\nSaindo do programa...")
            break
        else:
            type_text("\nOpção inválida! Por favor, escolha uma opção entre 1 e 4.")
        
        if opcao in ['1', '2', '3']:
            type_text("\nPressione Enter para continuar...")
            input()

menu()