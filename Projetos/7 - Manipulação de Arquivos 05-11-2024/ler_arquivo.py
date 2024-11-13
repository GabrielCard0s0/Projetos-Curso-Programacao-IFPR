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

def read_file_content(file_path):
    """
    Lê e exibe o conteúdo de um arquivo de texto.
    
    Parâmetros:
    file_path (str): O caminho do arquivo a ser lido.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        type_text(f"Conteúdo do arquivo '{file_path}':")
        type_text(content)
    except Exception as e:
        type_text(f"Erro ao ler o arquivo: {e}")

def menu():
    """
    Exibe o menu e solicita o caminho do arquivo a ser lido.
    """
    while True:
        type_text("Ler conteúdo de um arquivo de texto")
        file_path = input("Digite o caminho do arquivo (ex: 'caminho/arquivo.txt'): ")
        read_file_content(file_path)
        
        type_text("Pressione 'S' para sair ou qualquer outra tecla para continuar:")
        user_input = input().upper()
        if user_input == 'S':
            type_text("Saindo do programa...")
            break
menu()