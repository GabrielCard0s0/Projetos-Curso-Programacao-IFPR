
def Lista_Pessoas():
    quantidade = int(input("Quantos nomes você deseja inserir? "))

    nomes = []

    for i in range(quantidade):
        nome = input(f"Digite o nome {i + 1}: ")
        nomes.append(nome)

    nomes.sort()

    print("\nNomes em ordem alfabética:")
    for nome in nomes:
        print(nome)
        
Lista_Pessoas()