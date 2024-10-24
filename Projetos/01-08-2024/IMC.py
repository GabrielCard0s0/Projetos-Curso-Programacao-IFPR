# Exibe um cabeçalho para o cálculo de IMC
print('-'*30)
print('Cálculo de IMC.')
print('-'*30)

# Solicita ao usuário que informe o peso em kg
peso = float(input('Qual o peso? '))

# Solicita ao usuário que informe a altura em metros
altura = float(input('Qual a altura? '))

# Calcula o IMC usando a fórmula: IMC = peso / (altura ** 2)
imc = peso / (altura ** 2)

# Exibe o resultado do IMC formatado com duas casas decimais
print('-'*30)
print(f'{imc:.2f}')  # Corrigido para .2f para mostrar duas casas decimais
print('-'*30)
