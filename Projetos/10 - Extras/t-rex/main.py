import pygame
import random
import sys

# Inicializando o pygame
pygame.init()

# Definindo cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 300
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo do T-Rex")

# Definindo a taxa de atualização (FPS)
clock = pygame.time.Clock()

# Velocidade de movimento
GROUND_SPEED = 10
OBSTACLE_SPEED = 7
JUMP_VELOCITY = -15
GRAVITY = 0.5

# Definindo fontes
font = pygame.font.SysFont('Arial', 20)

# Função para desenhar o chão
def draw_ground(ground_x):
    pygame.draw.rect(screen, GREEN, (0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50))
    pygame.draw.rect(screen, BROWN, (ground_x, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50))

# Função para desenhar o T-Rex
def draw_trex(x, y):
    pygame.draw.rect(screen, BLACK, (x, y, 40, 40))  # Corpo do T-Rex
    pygame.draw.rect(screen, BLACK, (x + 10, y - 10, 20, 10))  # Cabeça
    pygame.draw.rect(screen, BLACK, (x + 25, y + 5, 5, 10))  # Cauda
    pygame.draw.rect(screen, BLACK, (x + 5, y + 30, 10, 10))  # Pernas

# Função para desenhar obstáculos
def draw_obstacle(x, y):
    pygame.draw.rect(screen, BLACK, (x, y, 20, 40))

# Função principal do jogo
def game_loop():
    # Posições iniciais
    trex_x = 50
    trex_y = SCREEN_HEIGHT - 90
    trex_velocity_y = 0
    on_ground = True

    # Obstáculos
    obstacle_x = SCREEN_WIDTH
    obstacle_y = SCREEN_HEIGHT - 90

    # Movimento do chão
    ground_x = 0

    # Pontuação
    score = 0

    # Loop principal do jogo
    while True:
        screen.fill(WHITE)

        # Checando eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and on_ground:
                    trex_velocity_y = JUMP_VELOCITY
                    on_ground = False

        # Atualizando a posição do T-Rex
        trex_y += trex_velocity_y
        if trex_y < SCREEN_HEIGHT - 90:
            trex_velocity_y += GRAVITY  # Simula a gravidade
        else:
            trex_y = SCREEN_HEIGHT - 90
            on_ground = True
            trex_velocity_y = 0

        # Atualizando a posição do obstáculo
        obstacle_x -= OBSTACLE_SPEED
        if obstacle_x < 0:
            obstacle_x = SCREEN_WIDTH
            score += 1

        # Atualizando o chão
        ground_x -= GROUND_SPEED
        if ground_x < -SCREEN_WIDTH:
            ground_x = 0

        # Desenhando tudo
        draw_ground(ground_x)
        draw_trex(trex_x, trex_y)
        draw_obstacle(obstacle_x, obstacle_y)

        # Desenhando a pontuação
        score_text = font.render(f"Pontos: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        # Verificando colisão com o obstáculo
        if (trex_x + 40 > obstacle_x and trex_x < obstacle_x + 20) and (trex_y + 40 > obstacle_y):
            game_over(score)

        # Atualizando a tela
        pygame.display.update()

        # Controlando o FPS
        clock.tick(60)

# Função de Game Over
def game_over(score):
    game_over_text = font.render(f"Game Over! Pontuação Final: {score}", True, BLACK)
    screen.fill(WHITE)
    screen.blit(game_over_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
    pygame.display.update()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

# Iniciando o jogo
game_loop()
