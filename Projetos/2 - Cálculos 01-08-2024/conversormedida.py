# Exibe um cabeçalho para o conversor
print('-'*30)
print('Conversor')
print('-'*30)

# Solicita ao usuário que digite uma distância em metros
valormetros = float(input('Digite a distancia em metros: '))

# Converte a distância de metros para quilômetros
conversor = valormetros / 1000

# Exibe a distância convertida, formatada para duas casas decimais
print('-'*30)
print(f'{conversor:.2f} km')  # Corrigido para .2f para mostrar duas casas decimais
print('-'*30)
