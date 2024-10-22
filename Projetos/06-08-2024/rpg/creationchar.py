import random
import time


class Personagem:
    def __init__(self, nome, classe, raca):
        self.nome = nome
        self.classe = classe
        self.raca = raca
        self.hp = self.rolar_dado(10)  # HP inicial é um valor aleatório entre 1 e 10
        self.forca = self.rolar_dado(6)
        self.destreza = self.rolar_dado(6)
        self.inteligencia = self.rolar_dado(6)

    def rolar_dado(self, lados):
        return random.randint(1, lados)

    def exibir_informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Classe: {self.classe}')
        print(f'Raça: {self.raca}')
        print(f'HP: {self.hp}')
        print(f'Força: {self.forca}')
        print(f'Destreza: {self.destreza}')
        print(f'Inteligência: {self.inteligencia}')

def criar_personagem():
    nome = input('Digite o nome do personagem: ')
    classe = input('Digite a classe do personagem (e.g., Guerreiro, Mago): ')
    raca = input('Digite a raça do personagem (e.g., Humano, Elfo): ')
    
    personagem = Personagem(nome, classe, raca)
    return personagem

def op1():
    


def exibir_informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Classe: {self.classe}')
        print(f'Raça: {self.raca}')
        print(f'HP: {self.hp}')
        print(f'Força: {self.forca}')
        print(f'Destreza: {self.destreza}')
        print(f'Inteligência: {self.inteligencia}')



def main():
    print('Bem-vindo ao Criador de Personagens RPG!')
    personagem = criar_personagem()
    print('\nInformações do personagem criado:')
    personagem.exibir_informacoes()
    print('Selecione uma opção:\n 1. Novo jogo\n 2. Exibir Personagem\n')
    personagem.exibir_informacoes()


if __name__ == '__main__':
    main()


