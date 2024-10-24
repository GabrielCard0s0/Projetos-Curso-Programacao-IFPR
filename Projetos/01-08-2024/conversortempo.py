# Solicita ao usuário que insira um tempo total em segundos
totalsegundos = int(input('Insira o tempo total em segundos: '))

# Calcula o número de horas
hora = totalsegundos // 3600

# Calcula o restante de segundos após extrair as horas
restohora = totalsegundos % 3600

# Calcula o número de minutos a partir do restante de segundos
minutos = restohora // 60

# Calcula os segundos restantes após extrair os minutos
segundos = restohora % 60

# Exibe o tempo total formatado em horas, minutos e segundos
print(hora, "hora(s)", minutos, "minuto(s)", segundos, "segundo(s):")