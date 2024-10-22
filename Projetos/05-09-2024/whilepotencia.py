base = float(input("Informe a base: "))
expoente = int(input("Informe o expoente: "))
resultado = 1
i = 1

while i <= expoente:
    resultado *= base
    i += 1

print(f"O resultado do cálculo é: {resultado}")