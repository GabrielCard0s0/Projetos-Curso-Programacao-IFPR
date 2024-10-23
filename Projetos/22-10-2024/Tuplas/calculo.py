import math
from math import sqrt

def Calculo(p1, p2):
    return math.sqrt((p1[0] - p2[0])** 2 + 
                     (p1[1] - p2[1])** 2 + 
                     (p1[2] - p2[2])** 2)

def main():
    x1 = float(input('valor de x1: '))
    y1 = float(input('valor de y1: '))
    z1 = float(input('valor de z1: '))

    ponto1 = (x1, y1, z1)

    x2 = float(input('valor de x2: '))
    y2 = float(input('valor de y2: '))
    z2 = float(input('valor de z2: '))

    ponto2 = (x2, y2, z2)

    print(Calculo(ponto1, ponto2))

main()