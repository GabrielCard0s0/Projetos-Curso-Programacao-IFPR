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

def save_name_to_file(full_name, file_path):
    """
    Salva o nome completo do usuário em um arquivo de texto.
    
    Parâmetros:
    full_name (str): O nome completo do usuário.
    file_path (str): O caminho do arquivo onde o dado será armazenado.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(full_name)
        type_text(f"Nome salvo com sucesso no arquivo: {file_path}")
    except Exception as e:
        type_text(f"Erro ao salvar o arquivo: {e}")

def menu():
    """
    Exibe o menu e solicita as informações do usuário.
    """
    while True:
        type_text("Salvar nome em arquivo de texto:")
        full_name = input("Digite seu nome completo: ")
        file_path = input("Digite o caminho do arquivo (ex: 'caminho/arquivo.txt'): ")
        save_name_to_file(full_name, file_path)
        
        type_text("Pressione 'S' para sair ou qualquer outra tecla para continuar:")
        user_input = input().upper()
        if user_input == 'S':
            type_text("Saindo do programa...")
            break

menu()