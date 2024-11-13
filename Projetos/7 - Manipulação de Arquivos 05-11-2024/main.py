import time

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

def Save_File(full_name, file_path):
    """
    Salva o nome completo do usuário em um arquivo de texto.
    
    Parâmetros:
    full_name (str): O nome completo do usuário.
    file_path (str): O caminho do arquivo onde o dado será armazenado.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(full_name)
        Type_Text(f"Nome salvo com sucesso no arquivo: {file_path}")
    except Exception as e:
        Type_Text(f"Erro ao salvar o arquivo: {e}")

def Read_Content(file_path):
    """
    Lê e exibe o conteúdo de um arquivo de texto.
    
    Parâmetros:
    file_path (str): O caminho do arquivo a ser lido.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        Type_Text(f"\nConteúdo do arquivo '{file_path}':")
        print("=" * 40)
        Type_Text(content)
        print("=" * 40)
    except Exception as e:
        Type_Text(f"Erro ao ler o arquivo: {e}")

def Count_Lines(file_path):
    """
    Conta e exibe o número total de linhas de um arquivo de texto.
    
    Parâmetros:
    file_path (str): O caminho do arquivo a ser analisado.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            total_lines = len(lines)
            
            Type_Text(f"\nAnálise do arquivo '{file_path}':")
            print("=" * 40)
            Type_Text(f"Total de linhas: {total_lines}")
            
            empty_lines = sum(1 for line in lines if line.strip() == '')
            Type_Text(f"Linhas em branco: {empty_lines}")
            Type_Text(f"Linhas com conteúdo: {total_lines - empty_lines}")
            
            if total_lines > 0:
                Type_Text("\nPrimeiras 5 linhas do arquivo (se existirem):")
                Type_Text("-" * 40)
                for i, line in enumerate(lines[:5], 1):
                    Type_Text(f"Linha {i}: {line.strip()}")
                    
    except Exception as e:
        Type_Text(f"Erro ao analisar o arquivo: {e}")

def Menu():
    """
    Exibe o menu principal com todas as opções disponíveis.
    """
    while True:
        Type_Text("\nGerenciador de Arquivos de Texto")
        print("=" * 40)
        Type_Text("1. Salvar nome em arquivo")
        Type_Text("2. Ler conteúdo do arquivo")
        Type_Text("3. Contar linhas do arquivo")
        Type_Text("4. Sair")
        print("=" * 40)
        
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == '1':
            Type_Text("\nSalvar nome em arquivo:")
            full_name = input("Digite o nome completo: ")
            file_path = input("Digite o caminho do arquivo: ")
            Save_File(full_name, file_path)
            
        elif opcao == '2':
            Type_Text("\nLer conteúdo do arquivo:")
            file_path = input("Digite o caminho do arquivo: ")
            Read_Content(file_path)
            
        elif opcao == '3':
            Type_Text("\nContar linhas do arquivo:")
            file_path = input("Digite o caminho do arquivo: ")
            Count_Lines(file_path)
            
        elif opcao == '4':
            Type_Text("\nSaindo do programa...")
            break
            
        else:
            Type_Text("\nOpção inválida! Por favor, escolha uma opção entre 1 e 4.")
        
        if opcao in ['1', '2', '3']:
            Type_Text("\nPressione Enter para continuar...")
            input()

Menu()