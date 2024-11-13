import math  # Importa o módulo math para funções matemáticas
from math import sqrt  # Importa a função sqrt diretamente

def Calculo(p1, p2):
    # Calcula a distância entre dois pontos em 3D usando a fórmula da distância
    return math.sqrt((p1[0] - p2[0]) ** 2 + 
                     (p1[1] - p2[1]) ** 2 + 
                     (p1[2] - p2[2]) ** 2)

def main():
    # Solicita ao usuário as coordenadas do primeiro ponto
    x1 = float(input('valor de x1: '))
    y1 = float(input('valor de y1: '))
    z1 = float(input('valor de z1: '))

    ponto1 = (x1, y1, z1)  # Cria uma tupla para o primeiro ponto

    # Solicita ao usuário as coordenadas do segundo ponto
    x2 = float(input('valor de x2: '))
    y2 = float(input('valor de y2: '))
    z2 = float(input('valor de z2: '))

    ponto2 = (x2, y2, z2)  # Cria uma tupla para o segundo ponto

    # Calcula e imprime a distância entre os dois pontos
    print(Calculo(ponto1, ponto2))

main()  # Chama a função principal para executar o programa
