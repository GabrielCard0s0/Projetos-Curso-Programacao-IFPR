print('-'*30)
print('Descubra se o ano é bissexto:')
print('-'*30)

ano = int(input('Digite o ano: '))  
print('-'*30)

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(ano, 'é um ano bissexto')
    print('-'*30)
else:
    print(ano, 'não é bissexto')
    print('-'*30)