# Exibe um cabeçalho para o programa de verificação de idade para votar
print('-'*30)
print('Tenho idade para voltar? Descubra:')
print('-'*30)

# Solicita ao usuário que digite sua idade
idade = int(input('Digite sua idade: '))

# Verifica se a idade é maior ou igual a 16
if idade >= 16:
    print('-'*30)
    print('Você já tem a idade necessária para votar!')
    print('-'*30)
else:
    print('-'*30)
    print('Você ainda não tem idade para votar.')
    print('-'*30)
