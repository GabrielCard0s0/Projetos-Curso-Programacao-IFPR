# Exibe um cabeçalho para o programa de verificação de ano bissexto
print('-'*30)
print('Descubra se o ano é bissexto:')
print('-'*30)

# Solicita ao usuário que digite um ano
ano = int(input('Digite o ano: '))  
print('-'*30)

# Verifica se o ano é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    # Se o ano for divisível por 4 e não por 100, ou divisível por 400, é bissexto
    print(ano, 'é um ano bissexto')
    print('-'*30)
else:
    # Caso contrário, não é bissexto
    print(ano, 'não é bissexto')
    print('-'*30)
