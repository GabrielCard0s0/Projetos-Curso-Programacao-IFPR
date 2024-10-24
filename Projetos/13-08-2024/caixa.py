# Exibe um cabeçalho de boas-vindas
print('-' * 30)
print('Bem-vindo ao Supermercado Xis')
print('-' * 30)

# Solicita o valor da compra ao usuário
valor = float(input('Digite o valor da compra: '))
print('-' * 30)

# Solicita a forma de pagamento
pagamento = int(input('Forma de pagamento:\n 1. à vista \n 2. a prazo\nOpção:'))
print('-' * 30)

# Verifica se a forma de pagamento é a prazo
if pagamento == 2:
    print('-' * 30)
    # Exibe as opções de parcelamento
    print('Parcelas:''\n1x sem juros', '\n2x sem juros', '\n3x sem juros', '\n4x sem juros', '\n5x sem juros', '\n6x sem juros')
    print('-' * 30)

    # Solicita o número de parcelas
    parcela = int(input('Digite o número de parcelas de 1 a 6: '))
    
    # Verifica se o número de parcelas está entre 1 e 6
    if 1 <= parcela <= 6:
        # Calcula o valor de cada parcela
        parcelado = valor / parcela
        print('-' * 30)
        print('Concluído!\n Parcelado em', parcela, 'vezes.')
        print('-' * 30)
        print('Valor de cada parcela:', '%.2f' % parcelado)  # Formata o valor da parcela
        print('-' * 30)
        print('Pagamento concluído!')
        print('-' * 30)
    else:
        print('Número de parcelas inválido!')

# Verifica se a forma de pagamento é à vista
elif pagamento == 1:
    print('-' * 30)
    print('Valor total:', valor)
    print('-' * 30)
    # Aplica um desconto de 10%
    desconto = valor * 0.9
    print('Valor com desconto:', desconto)
    print('-' * 30)
else:
    # Caso a opção de pagamento seja inválida
    print('Opção inválida!')
