texto = input("Digite um texto: ").lower()
vogais = 'aeiou'
contador = 0

for caractere in texto:
    if caractere in vogais:
        contador += 1

print(contador)      

