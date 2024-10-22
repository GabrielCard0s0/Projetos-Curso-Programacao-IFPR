def Primo(num):
    divisores = 0
    i = 1
    while i <= num:
        if num % i == 0:
            divisores += 1
        i += 1

    if divisores == 2:
        return True
    else:
        return False
    
#-------------------------

num_primos = []
num_nao_primos = []
num = int(input('Verificar primo até qual numero?'))

for e in range(2, num + 1):
    if Primo(e):
        num_primos.append(e)
    else:
        num_nao_primos.append(e)

print(f'Os numeros primos até {num} são: {num_primos} \nOs numeros não primos até {num} são: {num_nao_primos}')