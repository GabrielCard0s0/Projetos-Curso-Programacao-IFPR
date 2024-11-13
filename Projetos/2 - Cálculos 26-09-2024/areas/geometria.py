import math  # Importa o módulo math para usar funções matemáticas

# Calcula a área do quadrado
def Area_Quadrado(lado):
    return lado * lado

# Calcula a área do retângulo
def Area_Retangulo(base, altura):
    return base * altura

# Calcula a área do triângulo
def Area_Triangulo(base, altura):
    return (base * altura) / 2

# Calcula a área do círculo
def Area_Circulo(raio):
    return math.pi * raio ** 2  # Usa pi da biblioteca math para maior precisão
