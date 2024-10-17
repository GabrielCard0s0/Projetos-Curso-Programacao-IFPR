from distancia import km_para_milhas, milhas_para_km

def main():
    options = {
        '1': 'Quilômetros para Milhas',
        '2': 'Milhas para Quilômetros',
        '0': 'Sair'
    }

    while True:
        print("\nBem-vindo à calculadora de conversão de distâncias!")
        print("Escolha a conversão desejada:")
        
        for key, value in options.items():
            print(f"{key} - {value}")
        
        escolha = input("Digite o número da opção desejada (1, 2 ou 0): ")
        
        try:
            if escolha == '1':
                km = float(input("Digite a distância em quilômetros: "))
                milhas = km_para_milhas(km)
                print(f"{km:.2f} quilômetros são {milhas:.2f} milhas.")
            elif escolha == '2':
                milhas = float(input("Digite a distância em milhas: "))
                km = milhas_para_km(milhas)
                print(f"{milhas:.2f} milhas são {km:.2f} quilômetros.")
            elif escolha == '0':
                print("Saindo do programa. Até logo!")
                break
            else:
                print("Opção inválida. Por favor, escolha 1, 2 ou 0.")
        
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

main()
