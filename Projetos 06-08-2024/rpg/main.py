from creationchar import Personagem, main, criar_personagem, exibir_informacoes


import time

print('-'*30)
print('RPG Python')
print('-'*30)

time.sleep(2)

print('-'*30)
main()
print('-'*30)

time.sleep(2)

print('-'*30)
print('Escolha uma opção:\n')
print('-'*30)
opção1 = int(input("1. Iniciar Novo Jogo\n 2. Exibir informações do personagem\n 3. Reiniciar\n" ))
if opção1 == 1:
    main()
elif opção1 == 2:
    mostrar = self.exibir_informacoes()
    print(mostrar)
elif opção1 == 3:
    main()