import random

def adivinhacao():
    numero_secreto = random.randint(0, 10)
    tentativas = 3

    print("Bem-vindo ao jogo de adivinhação!")
    print("Eu pensei em um número entre 0 e 10. Você tem 3 tentativas para adivinhar.")

    for tentativa in range(tentativas):
        palpite = int(input(f"Tentativa {tentativa + 1}: Informe seu palpite: "))

        if palpite < 0 or palpite > 10:
            print("Por favor, escolha um número entre 0 e 10.")
            continue

        if palpite == numero_secreto:
            print("Parabéns! Você adivinhou o número!")
            break
        else:
            if tentativa < tentativas - 1:
                print("Errado! Tente novamente.")
            else:
                print(f"Você perdeu! O número secreto era {numero_secreto}.")


adivinhacao()