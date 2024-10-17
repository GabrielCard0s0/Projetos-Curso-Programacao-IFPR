total = 0


continuar = True

while continuar != False:
    entrada = input("Digite um número ou 'Fim' para encerrar: ")
        
    if entrada == 'Fim':
        continuar = False
    else:
        numero = float(entrada)
        total += numero
    print(f"A soma parcial é: {total}")

print(f"A soma total é: {total}")
print('Fim...')
