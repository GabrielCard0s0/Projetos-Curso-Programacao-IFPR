import time

def Digitar(texto, atraso=0.03):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(atraso)
    print()

def charada():
    Digitar("O que é, o que é que está sempre a caminho, mas nunca chega?")
    
    try:
        resposta = input("> ")
    except Exception as e:
        Digitar(f"Ocorreu um erro ao receber a resposta: {e}")
        return

    dicas = [
        "É algo que todos esperam.",
        "Vem depois de hoje.",
        "É um conceito de tempo."
    ]
    
    tentativas_dica = 0

    while tentativas_dica < 4:
        if resposta.lower() == "amanhã":
            Digitar("Correto! Você acertou!")
            return
        else:
            pedir_dica = input("Você quer uma dica? (s/n): ")
            try:
                if pedir_dica.lower() == 's':
                    Digitar(dicas[tentativas_dica])
                    tentativas_dica += 1
                else:
                    resposta = input("Digite sua resposta: ")
            except IndexError:
                Digitar("Você já usou todas as dicas disponíveis.")
                break
            except Exception as e:
                Digitar(f"Ocorreu um erro: {e}")
                return
    
    Digitar("Você perdeu! A resposta correta é 'amanhã'.")

charada()