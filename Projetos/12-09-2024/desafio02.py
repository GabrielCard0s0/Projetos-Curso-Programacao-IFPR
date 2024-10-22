
n = int(input("Digite o valor de n (número inteiro positivo): "))

if n == 1 or n == 2:
    
    resultado = 1

else:
    ultimo = 1
    atual = 1
    i = 3
    while i <= n:
        proximo = ultimo + atual
       
        ultimo = atual 
        atual = proximo
        i += 1
   
    resultado = atual


print(f"O {n}º termo da sequência de Fibonacci é: {resultado}")