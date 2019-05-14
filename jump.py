# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
import random
from os import path

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'img')

# Dados gerais do jogo.
TITULO = 'Exemplo de Pulo'
WIDTH = 480 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define a aceleração da gravidade
GRAVITY = 2
# Define a velocidade inicial no pulo
JUMP_SIZE = 30
# Define a altura do chão
GROUND = HEIGHT * 5 // 6

# Define estados possíveis do jogador
STILL = 0
JUMPING = 1
FALLING = 2

# Classe Jogador que representa o herói
class Player(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, player_img):

        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Define estado atual
        # Usamos o estado para decidir se o jogador pode ou não pular
        self.state = STILL

        # Aumenta o tamanho da imagem para ficar mais fácil de ver
        player_img = pygame.transform.scale(player_img, (100, 160))

        # Define a imagem do sprite. Nesse exemplo vamos usar uma imagem estática (não teremos animação durante o pulo)
        self.image = player_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Começa no topo da janela e cai até o chão
        self.rect.centerx = WIDTH / 2
        self.rect.top = 0

        self.speedy = 0

    # Metodo que atualiza a posição do personagem
    def update(self):
        self.speedy += GRAVITY
        # Atualiza o estado para caindo
        if self.speedy > 0:
            self.state = FALLING
        self.rect.y += self.speedy
        # Se bater no chão, para de cair
        if self.rect.bottom > GROUND:
            # Reposiciona para a posição do chão
            self.rect.bottom = GROUND
            # Para de cair
            self.speedy = 0
            # Atualiza o estado para parado
            self.state = STILL

    # Método que faz o personagem pular
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING


def game_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega imagem
    player_img = pygame.image.load(path.join(img_dir, 'hero-single.png')).convert_alpha()

    # Cria Sprite do jogador
    player = Player(player_img)
    # Cria um grupo de todos os sprites e adiciona o jogador.
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    PLAYING = 0
    DONE = 1

    state = PLAYING
    while state != DONE:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():

            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = DONE

            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    player.jump()

        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite. O grupo chama o método update() de cada Sprite dentre dele.
        all_sprites.update()

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()


# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption(TITULO)

# Imprime instruções
print('*' * len(TITULO))
print(TITULO.upper())
print('*' * len(TITULO))
print('Utilize a tecla "ESPAÇO" ou seta para cima para pular.')

# Comando para evitar travamentos.
try:
    game_screen(screen)
finally:
    pygame.quit()
