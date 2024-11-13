from distancia import km_para_milhas, milhas_para_km  # Importa as funções de conversão

def main():
    # Dicionário para armazenar as opções de conversão
    options = {
        '1': 'Quilômetros para Milhas',
        '2': 'Milhas para Quilômetros',
        '0': 'Sair'
    }

    while True:
        print("\nBem-vindo à calculadora de conversão de distâncias!")  # Mensagem de boas-vindas
        print("Escolha a conversão desejada:")
        
        # Exibe as opções disponíveis
        for key, value in options.items():
            print(f"{key} - {value}")
        
        escolha = input("Digite o número da opção desejada (1, 2 ou 0): ")
        
        try:
            # Conversão de quilômetros para milhas
            if escolha == '1':
                km = float(input("Digite a distância em quilômetros: "))  # Lê a distância em km
                milhas = km_para_milhas(km)  # Chama a função de conversão
                print(f"{km:.2f} quilômetros são {milhas:.2f} milhas.")  # Exibe o resultado
            
            # Conversão de milhas para quilômetros
            elif escolha == '2':
                milhas = float(input("Digite a distância em milhas: "))  # Lê a distância em milhas
                km = milhas_para_km(milhas)  # Chama a função de conversão
                print(f"{milhas:.2f} milhas são {km:.2f} quilômetros.")  # Exibe o resultado
            
            # Sair do programa
            elif escolha == '0':
                print("Saindo do programa. Até logo!")
                break
            
            # Caso a opção não seja válida
            else:
                print("Opção inválida. Por favor, escolha 1, 2 ou 0.")
        
        except ValueError:  # Trata erros de entrada
            print("Entrada inválida. Por favor, insira um número válido.")

main()  # Chama a função principal para iniciar o programa
