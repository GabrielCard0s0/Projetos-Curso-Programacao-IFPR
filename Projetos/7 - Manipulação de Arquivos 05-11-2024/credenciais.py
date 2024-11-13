import time
import os

def Type_Text(text, delay=0.05):
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

def Create_Credentials_File(file_path):
    """
    Cria o arquivo de credenciais se ele não existir.
    
    Parâmetros:
    file_path (str): Caminho do arquivo a ser criado
    """
    if not os.path.exists(file_path):
        try:
            with open(file_path, 'w') as file:
                file.write("admin\n")  # usuário padrão
                file.write("123456\n") # senha padrão
            Type_Text(f"\nArquivo de credenciais criado em: {file_path}")
            Type_Text("Usuário padrão: admin")
            Type_Text("Senha padrão: 123456")
        except Exception as e:
            Type_Text(f"Erro ao criar arquivo de credenciais: {e}")

def Verify_Credentials(username, password, file_path):
    """
    Verifica as credenciais do usuário com os dados do arquivo.
    
    Parâmetros:
    username (str): Nome de usuário informado
    password (str): Senha informada
    file_path (str): Caminho do arquivo com as credenciais
    """
    try:
        if not os.path.exists(file_path):
            Create_Credentials_File(file_path)
            
        with open(file_path, 'r') as file:
            stored_username = file.readline().strip()
            stored_password = file.readline().strip()
            
            if username == stored_username and password == stored_password:
                Type_Text("\nLogin realizado com sucesso!")
                return True
            else:
                Type_Text("\nUsuário ou senha incorretos!")
                return False
                
    except Exception as e:
        Type_Text(f"Erro ao ler o arquivo de credenciais: {e}")
        return False

def Menu():
    """
    Exibe o menu e solicita as credenciais do usuário.
    """
    # Obtém o diretório atual onde o script está sendo executado
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "credenciais.txt")
    
    # Cria o arquivo de credenciais se não existir
    if not os.path.exists(file_path):
        Create_Credentials_File(file_path)
    
    while True:
        Type_Text("\nSistema de Autenticação")
        print("=" * 30)
        Type_Text("1. Fazer Login")
        Type_Text("2. Sair")
        print("=" * 30)
        
        opcao = input("Escolha uma opção (1 ou 2): ")
        
        if opcao == '1':
            Type_Text("\nPor favor, informe suas credenciais:")
            username = input("Usuário: ")
            password = input("Senha: ")
            
            Verify_Credentials(username, password, file_path)
            
            Type_Text("\nPressione Enter para continuar...")
            input()
            
        elif opcao == '2':
            Type_Text("\nSaindo do sistema...")
            break
        else:
            Type_Text("\nOpção inválida! Por favor, escolha 1 ou 2.")

Menu()