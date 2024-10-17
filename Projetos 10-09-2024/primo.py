
print(f'Digite um numero para saber se ele é primo:')
number = int(input('> '))
divisor = 0

i = 1
while i <= number:
    if  number % i == 0:
        divisor += 1
    i += 1

if divisor == 2:      
    print(f'{number} é primo.')
else:
    print(f'{number} não é primo.')
                
    
