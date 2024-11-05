import time

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

def count_file_lines(file_path):
    """
    Conta e exibe o número total de linhas de um arquivo de texto.
    
    Parâmetros:
    file_path (str): O caminho do arquivo a ser analisado.
    """
    try:
        with open(file_path, 'r') as file:
            # Lê todas as linhas do arquivo
            lines = file.readlines()
            total_lines = len(lines)
            
            # Exibe o número total de linhas
            type_text(f"\nAnálise do arquivo '{file_path}':")
            type_text(f"Total de linhas: {total_lines}")
            
            # Exibe detalhes adicionais
            empty_lines = sum(1 for line in lines if line.strip() == '')
            type_text(f"Linhas em branco: {empty_lines}")
            type_text(f"Linhas com conteúdo: {total_lines - empty_lines}")
            
            # Exibe uma amostra das primeiras linhas
            if total_lines > 0:
                type_text("\nPrimeiras 5 linhas do arquivo (se existirem):")
                for i, line in enumerate(lines[:5], 1):
                    type_text(f"Linha {i}: {line.strip()}")
                    
    except Exception as e:
        type_text(f"Erro ao analisar o arquivo: {e}")

def menu():
    """
    Exibe o menu e solicita o caminho do arquivo a ser analisado.
    """
    while True:
        type_text("\nContador de linhas de arquivo de texto")
        print("=" * 40)
        type_text("1. Analisar arquivo")
        type_text("2. Sair")
        print("=" * 40)
        
        opcao = input("Escolha uma opção (1 ou 2): ")
        
        if opcao == '1':
            file_path = input("\nDigite o caminho do arquivo (ex: 'caminho/arquivo.txt'): ")
            count_file_lines(file_path)
        elif opcao == '2':
            type_text("\nSaindo do programa...")
            break
        else:
            type_text("\nOpção inválida! Por favor, escolha 1 ou 2.")
        
        if opcao == '1':
            type_text("\nPressione Enter para continuar...")
            input()

menu()