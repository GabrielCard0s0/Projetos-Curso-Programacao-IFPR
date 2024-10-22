print('-'*30)
print('Vamos calcular o IMC.')
print('-'*30)

print('-'*30)
peso = float(input('Digite o peso em KG:'))
print('-'*30)

print('-'*30)
altura = float(input('Digite a altura em metros:'))
print('-'*30)


imc = peso / (altura ** 2)

# Classificação do IMC
if imc >= 30: 
    print('-'*30)
    print("O IMC é de","%.2f" % imc, "\n" "Classificação: Obesidade.")
    print('-'*30)
elif 26 <= imc < 30:
    print('-'*30)
    print("O IMC é de","%.2f" % imc, "\n" 'Classificação: Acima do peso.')
    print('-'*30)
elif 18.6 <= imc < 26:
    print('-'*30)
    print("O IMC é de","%.2f" % imc, "\n" 'Classificação: Normal.')
    print('-'*30)
else:
    print('-'*30)
    print("O IMC é de","%.2f" % imc, "\n" "Classificação: Abaixo do peso")