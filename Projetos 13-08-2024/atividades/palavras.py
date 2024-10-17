print('-'*30)
print('Vamos colocar as palavras em ordem alfabética.')
print('-'*30)

palavra1 = input("Digite a primeira palavra: ")
print('-'*30)
palavra2 = input("Digite a segunda palavra: ")
print('-'*30)
palavra3 = input("Digite a terceira palavra: ")
print('-'*30)

if palavra1 <= palavra2 and palavra1 <= palavra3:
    if palavra2 <= palavra3:
        print('-'*30)
        print('Palavras em ordem alfabetica:', '\n1.', palavra1, '\n2.', palavra2, '\n3.', palavra3)
        print('-'*30)
    else:
        print('-'*30)
        print('Palavras em ordem alfabetica:', '\n1.', palavra1, '\n2.', palavra3, '\n3.', palavra2)
        print('-'*30)
elif palavra2 <= palavra1 and palavra2 <= palavra3:
    if palavra1 <= palavra3:
        print('-'*30)
        print('Palavras em ordem alfabetica:', '\n1.', palavra2, '\n2.', palavra1, '\n3.', palavra3)
        print('-'*30)
    else:
        print('-'*30)
        print('Palavras em ordem alfabetica:','\n1.', palavra2, '\n2.', palavra3, '\n3.', palavra1)
        print('-'*30)
else:
    if palavra1 <= palavra2:
        print('-'*30)
        print('Palavras em ordem alfabetica:','\n1.', palavra3, '\n2.', palavra1, '\n3.', palavra2)
        print('-'*30)
    else:
        print('-'*30)
        print('Palavras em ordem alfabetica:','\n1.', palavra3, '\n2.', palavra2, '\n3.', palavra1)
        print('-'*30)