import time

# Listas para armazenar os nomes dos estudantes em cada atividade
atletismo = []
basquete = []

# Função para adicionar um estudante à lista correspondente ao tipo de atividade
def Add_Estudante(tipo, estudante):
    if tipo == 1:  # Se tipo for 1, adiciona à lista de atletismo
        atletismo.append(estudante)
    elif tipo == 2:  # Se tipo for 2, adiciona à lista de basquete
        basquete.append(estudante)

# Função para imprimir texto letra por letra, com um atraso entre as letras
def Digitar(texto, atraso=0.05):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(atraso)

# Função para verificar estudantes que estão em ambas as atividades
def Verificar():
    verificar = set(atletismo) & set(basquete)  # Encontra a interseção entre os conjuntos
    return list(verificar)  # Retorna a lista de estudantes simultâneos

# Função principal que exibe o menu e gerencia as escolhas do usuário
def Menu_Principal():
    while True:
        # Opções disponíveis no menu
        options = [
            '[1] Adicionar estudante',
            '[2] Ver estudantes em ambas as atividades',
            '[3] Sair',
        ]
        # Exibe as opções do menu
        for option in options:
            Digitar(option + '\n')
        
        try:
            Digitar('Escolha uma opção: ')
            escolha = int(input('> '))  # Lê a escolha do usuário
            
            if escolha == 1:  # Opção para adicionar estudante
                while True:
                    # Opções para escolher a atividade
                    options2 = [
                        '[1] Adicionar ao atletismo',
                        '[2] Adicionar ao basquete'
                    ]
                    for option in options2:
                        Digitar(option + '\n')
                    
                    Digitar('Escolha uma opção: ')
                    escolha_esporte = int(input('> '))
                    
                    if escolha_esporte in [1, 2]:  # Verifica se a escolha é válida
                        Digitar('Digite o nome do aluno: ')
                        nome_aluno = input('> ')
                        Add_Estudante(escolha_esporte, nome_aluno)  # Adiciona o aluno
                        Digitar(f'Aluno {nome_aluno} adicionado com sucesso!\n')
                    else:
                        Digitar('Digite uma opção válida!\n')
                    
                    Digitar('Deseja adicionar outro estudante? (s/n): ')
                    continuar = input('> ').strip().lower()  # Pergunta se deseja continuar
                    if continuar != 's':  # Se não, sai do loop
                        break

            elif escolha == 2:  # Opção para ver estudantes em ambas as atividades
                estudantes_simultaneos = Verificar()
                if estudantes_simultaneos:
                    Digitar('Estudantes que praticam ambas as atividades:\n')
                    for estudante in estudantes_simultaneos:
                        Digitar(f'- {estudante}\n')
                else:
                    Digitar('Nenhum estudante está praticando ambas as atividades.\n')
            
            elif escolha == 3:  # Opção para sair do programa
                Digitar('Finalizando...\n')
                break
            else:
                Digitar('Digite uma opção válida!\n')  # Se opção inválida, pede novamente
                time.sleep(1)
        
        except ValueError:
            Digitar('Escolha uma opção válida!\n')  # Se entrada não for um número, pede novamente
            time.sleep(1)

# Chama a função principal para iniciar o programa
Menu_Principal()