# Solicita ao usuário que digite um número inteiro positivo
n = int(input("Digite o valor de n (número inteiro positivo): "))

# Verifica se n é 1 ou 2, pois o primeiro e o segundo termos da sequência de Fibonacci são 1
if n == 1 or n == 2:
    resultado = 1  # O resultado é 1 para os dois primeiros termos

else:
    # Inicializa os dois primeiros termos da sequência
    ultimo = 1  # Último termo
    atual = 1   # Atual termo
    i = 3       # Começa a contagem a partir do terceiro termo
    
    # Loop para calcular os termos subsequentes da sequência de Fibonacci
    while i <= n:
        proximo = ultimo + atual  # O próximo termo é a soma dos dois anteriores
       
        # Atualiza os termos para a próxima iteração
        ultimo = atual 
        atual = proximo
        i += 1  # Incrementa o contador para passar para o próximo termo
   
    resultado = atual  # O termo atual será o n-ésimo termo

# Exibe o resultado
print(f"O {n}º termo da sequência de Fibonacci é: {resultado}")
