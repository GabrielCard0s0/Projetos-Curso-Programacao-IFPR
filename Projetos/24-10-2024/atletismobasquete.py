import time

atletismo = []
basquete = []

def Add_Estudante(tipo, estudante):
    if tipo == 1:
        atletismo.append(estudante)
    elif tipo == 2:
        basquete.append(estudante)

def Digitar(texto, atraso=0.05):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(atraso)
    

def Verificar():
    verificar = set(atletismo) and set(basquete)
    return list(verificar)

def Menu_Principal():
    while True:
        options = [
            '[1] Adicionar estudante',
            '[2] Ver estudantes em ambas as atividades',
            '[3] Sair',
        ]
        for option in options:
            Digitar(option + '\n')
        
        try:
            Digitar('Escolha uma opção: ')
            escolha = int(input('> '))
            
            if escolha == 1:
                while True:
                    options2 = [
                        '[1] Adicionar ao atletismo',
                        '[2] Adicionar ao basquete'
                    ]
                    for option in options2:
                        Digitar(option + '\n')
                    
                    Digitar('Escolha uma opção: ')
                    escolha_esporte = int(input('> '))
                    
                    if escolha_esporte in [1, 2]:
                        Digitar('Digite o nome do aluno: ')
                        nome_aluno = input('> ')
                        Add_Estudante(escolha_esporte, nome_aluno)
                        Digitar(f'Aluno {nome_aluno} adicionado com sucesso!\n')
                    else:
                        Digitar('Digite uma opção válida!\n')
                    
                    Digitar('Deseja adicionar outro estudante? (s/n): ')
                    continuar = input('> ').strip().lower()
                    if continuar != 's':
                        break

            elif escolha == 2:
                estudantes_simultaneos = Verificar()
                if estudantes_simultaneos:
                    Digitar('Estudantes que praticam ambas as atividades:\n')
                    for estudante in estudantes_simultaneos:
                        Digitar(f'- {estudante}\n')
                else:
                    Digitar('Nenhum estudante está praticando ambas as atividades.\n')
            
            elif escolha == 3:
                Digitar('Finalizando...\n')
                break
            else:
                Digitar('Digite uma opção válida!\n')
                time.sleep(1)
        
        except ValueError:
            Digitar('Escolha uma opção válida!\n')
            time.sleep(1)

Menu_Principal()