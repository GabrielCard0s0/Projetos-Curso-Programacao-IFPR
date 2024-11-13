# Solicita ao usuário que informe a base
base = float(input("Informe a base: "))

# Solicita ao usuário que informe o expoente
expoente = int(input("Informe o expoente: "))

# Inicializa a variável resultado como 1 (base de multiplicação)
resultado = 1

# Inicializa o contador
i = 1

# Loop que multiplica a base pelo resultado, expoente vezes
while i <= expoente:
    resultado *= base  # Multiplica o resultado pela base
    i += 1  # Incrementa o contador

# Exibe o resultado do cálculo da potência
print(f"O resultado do cálculo é: {resultado}")
