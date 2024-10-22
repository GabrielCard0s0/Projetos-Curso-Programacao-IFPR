import random


numero1a10 = float(input('Digite um numero de 1 a 10\n'))
gerar1a10 = random.randrange(1,10)

if numero1a10 == gerar1a10:
    print('-'*30)
    print('Você acertou! onumero correto é:\n', gerar1a10)
    print('-'*30)
    

else:
    print('-'*30)
    print('Você errou! O numero correto é:\n', gerar1a10)
    print('-'*30)
    