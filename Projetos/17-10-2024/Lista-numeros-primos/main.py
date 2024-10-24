def Primo(num):
    # Inicializa a contagem de divisores
    divisores = 0
    i = 1
    # Loop para contar os divisores do número
    while i <= num:
        if num % i == 0:  # Verifica se i é um divisor de num
            divisores += 1  # Incrementa a contagem de divisores
        i += 1  # Incrementa i para verificar o próximo número

    # Um número é primo se tem exatamente 2 divisores: 1 e ele mesmo
    if divisores == 2:
        return True
    else:
        return False

#-------------------------

# Listas para armazenar números primos e não primos
num_primos = []
num_nao_primos = []
# Solicita ao usuário um número para verificar primos até esse valor
num = int(input('Verificar primo até qual número? '))

# Loop para verificar cada número de 2 até o número fornecido
for e in range(2, num + 1):
    if Primo(e):  # Se e for primo
        num_primos.append(e)  # Adiciona à lista de primos
    else:
        num_nao_primos.append(e)  # Adiciona à lista de não primos

# Exibe os resultados
print(f'Os números primos até {num} são: {num_primos} \nOs números não primos até {num} são: {num_nao_primos}')
