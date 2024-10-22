import math

totalsegundos = int(input('Insira o tempo total em segundos: '))
hora = totalsegundos // 3600
restohora = totalsegundos % 3600
minutos = restohora // 60
segundos = restohora % 60

print( hora, "hora(s)", minutos, "minuto(s)", segundos, "segundo(s):")

