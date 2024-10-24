# Inicializa a variável total para armazenar a soma dos números
total = 0

# Inicializa a variável para controlar o loop
continuar = True

# Loop que continua até que o usuário decida encerrar
while continuar:
    # Solicita ao usuário que digite um número ou 'Fim' para encerrar
    entrada = input("Digite um número ou 'Fim' para encerrar: ")
        
    # Verifica se o usuário deseja encerrar o programa
    if entrada == 'Fim':
        continuar = False  # Altera a variável para sair do loop
    else:
        # Converte a entrada em um número e adiciona ao total
        numero = float(entrada)
        total += numero  # Acumula a soma dos números
    # Exibe a soma parcial até o momento
    print(f"A soma parcial é: {total}")

# Exibe a soma total após o encerramento
print(f"A soma total é: {total}")
print('Fim...')
