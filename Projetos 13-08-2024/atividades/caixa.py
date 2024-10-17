print('-'*30)
print('Bem-vindo ao Supermercado Xis')
print('-'*30)

valor = float(input('Digite o valor da compra: '))
print('-'*30)
pagamento = int(input('Forma de pagamento:\n 1. à vista \n 2. a prazo\nOpção:'))
print('-'*30)

if pagamento == 2:
    print('-'*30)
    print('Parcelas:''\n1x sem juros', '\n2x sem juros', '\n3x sem juros', '\n4x sem juros', '\n5x sem juros', '\n6x sem juros')
    print('-'*30)
    parcela = int(input('Digite o numero de parcelas de 1 a 6: '))
    if parcela >= 1 < 7:
        parcelado = valor / parcela
        print('-'*30)
        print('Concluido!\n Parcelado em', parcela, 'vezes.')
        print('-'*30)
        print('Valor de cada parcela:', '%.2f' %parcelado)
        print('-'*30)
        print('Pagamento concluido!')
        print('-'*30)
    else:
        print('Numero de parcelas inválido!')
elif pagamento == 1:
    print('-'*30)
    print('Valor total:', valor)
    print('-'*30)
    desconto = valor * .9
    print('Valor com desconto:', desconto)
    print('-'*30)
else:
    print('Opção inválida!')