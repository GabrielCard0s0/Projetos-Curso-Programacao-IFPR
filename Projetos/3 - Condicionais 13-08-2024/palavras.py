# Exibe um cabeçalho para o programa de ordenação de palavras
print('-' * 30)
print('Vamos colocar as palavras em ordem alfabética.')
print('-' * 30)

# Solicita que o usuário digite três palavras
palavra1 = input("Digite a primeira palavra: ")
print('-' * 30)
palavra2 = input("Digite a segunda palavra: ")
print('-' * 30)
palavra3 = input("Digite a terceira palavra: ")
print('-' * 30)

# Compara as palavras para determinar a ordem alfabética
if palavra1 <= palavra2 and palavra1 <= palavra3:
    # Se palavra1 é a menor
    if palavra2 <= palavra3:
        # palavra1 <= palavra2 <= palavra3
        print('-' * 30)
        print('Palavras em ordem alfabética:', '\n1.', palavra1, '\n2.', palavra2, '\n3.', palavra3)
        print('-' * 30)
    else:
        # palavra1 <= palavra3 < palavra2
        print('-' * 30)
        print('Palavras em ordem alfabética:', '\n1.', palavra1, '\n2.', palavra3, '\n3.', palavra2)
        print('-' * 30)
elif palavra2 <= palavra1 and palavra2 <= palavra3:
    # Se palavra2 é a menor
    if palavra1 <= palavra3:
        # palavra2 <= palavra1 <= palavra3
        print('-' * 30)
        print('Palavras em ordem alfabética:', '\n1.', palavra2, '\n2.', palavra1, '\n3.', palavra3)
        print('-' * 30)
    else:
        # palavra2 <= palavra3 < palavra1
        print('-' * 30)
        print('Palavras em ordem alfabética:', '\n1.', palavra2, '\n2.', palavra3, '\n3.', palavra1)
        print('-' * 30)
else:
    # Se palavra3 é a menor
    if palavra1 <= palavra2:
        # palavra3 <= palavra1 <= palavra2
        print('-' * 30)
        print('Palavras em ordem alfabética:', '\n1.', palavra3, '\n2.', palavra1, '\n3.', palavra2)
        print('-' * 30)
    else:
        # palavra3 <= palavra2 < palavra1
        print('-' * 30)
        print('Palavras em ordem alfabética:', '\n1.', palavra3, '\n2.', palavra2, '\n3.', palavra1)
        print('-' * 30)
