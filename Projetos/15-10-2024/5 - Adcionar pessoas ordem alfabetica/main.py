def Lista_Pessoas():
    # Pergunta ao usuário quantos nomes deseja inserir
    quantidade = int(input("Quantos nomes você deseja inserir? "))

    nomes = []  # Lista para armazenar os nomes

    # Loop para coletar os nomes
    for i in range(quantidade):
        nome = input(f"Digite o nome {i + 1}: ")
        nomes.append(nome)  # Adiciona o nome à lista

    nomes.sort()  # Ordena os nomes em ordem alfabética

    # Exibe os nomes ordenados
    print("\nNomes em ordem alfabética:")
    for nome in nomes:
        print(nome)

Lista_Pessoas()  # Chama a função para executar
