import random, time  # Importa as bibliotecas necessárias

# Função para imprimir texto letra por letra com um atraso
def Digitar(texto, atraso=0.05):
    for letra in texto:
        print(letra, end='', flush=True)  # Imprime a letra sem quebrar a linha
        time.sleep(atraso)  # Espera um tempo definido antes de imprimir a próxima letra

# Lista para armazenar os valores aleatórios
valores = []

# Gera 100 valores aleatórios entre 0 e 1000 e os adiciona à lista
for e in range(100):
    valor = random.randint(0, 1000)
    valores.append(valor)

# Loop principal do programa
while True:
    print(valores)  # Exibe a lista de valores
    Digitar('Informe o índice:')  # Solicita ao usuário que informe um índice
    try:
        indice = int(input('> '))  # Lê o índice informado pelo usuário
        print('-' * 50)
        print(valores[indice - 1])  # Exibe o valor correspondente ao índice (ajustando para zero)
        print('-' * 50)
        time.sleep(1)  # Espera 1 segundo antes de repetir o loop
    except ValueError:
        Digitar('Tente uma opção válida!')  # Mensagem de erro se a entrada não for um número
    except IndexError:
        Digitar('Índice fora do alcance!')  # Mensagem de erro se o índice não estiver na lista
