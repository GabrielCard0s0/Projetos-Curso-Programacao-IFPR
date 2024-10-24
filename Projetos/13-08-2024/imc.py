# Exibe um cabeçalho para o cálculo do IMC
print('-' * 30)
print('Vamos calcular o IMC.')
print('-' * 30)

# Solicita o peso do usuário em kg
print('-' * 30)
peso = float(input('Digite o peso em KG:'))
print('-' * 30)

# Solicita a altura do usuário em metros
print('-' * 30)
altura = float(input('Digite a altura em metros:'))
print('-' * 30)

# Calcula o IMC utilizando a fórmula: IMC = peso / (altura ** 2)
imc = peso / (altura ** 2)

# Classificação do IMC com base no resultado
if imc >= 30: 
    print('-' * 30)
    print("O IMC é de", "%.2f" % imc, "\n" "Classificação: Obesidade.")
    print('-' * 30)
elif 26 <= imc < 30:
    print('-' * 30)
    print("O IMC é de", "%.2f" % imc, "\n" 'Classificação: Acima do peso.')
    print('-' * 30)
elif 18.6 <= imc < 26:
    print('-' * 30)
    print("O IMC é de", "%.2f" % imc, "\n" 'Classificação: Normal.')
    print('-' * 30)
else:
    print('-' * 30)
    print("O IMC é de", "%.2f" % imc, "\n" "Classificação: Abaixo do peso")
