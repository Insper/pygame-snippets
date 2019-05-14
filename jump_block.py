# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
import random
from os import path

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'img')

# Dados gerais do jogo.
TITULO = 'Exemplo de Pulo com obstáculos'
WIDTH = 480 # Largura da tela
HEIGHT = 600 # Altura da tela
TILE_SIZE = 40 # Tamanho de cada tile (cada tile é um quadrado)
PLAYER_WIDTH = TILE_SIZE
PLAYER_HEIGHT = int(TILE_SIZE * 1.5)
FPS = 60 # Frames por segundo

# Imagens
PLAYER_IMG = 'player_img'

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define a aceleração da gravidade
GRAVITY = 5
# Define a velocidade inicial no pulo
JUMP_SIZE = TILE_SIZE
# Define a velocidade em x
SPEED_X = 5


# Define os tipos de tiles
BLOCK = 0
EMPTY = -1

# Define o mapa com os tipos de tiles
MAP = [
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY],
    [BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK],
    [EMPTY, EMPTY, BLOCK, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, BLOCK, BLOCK, BLOCK],
    [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
    [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
]

# Define estados possíveis do jogador
STILL = 0
JUMPING = 1
FALLING = 2

# Class que representa os blocos do cenário
class Tile(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, tile_img, row, column):
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Aumenta o tamanho do tile.
        tile_img = pygame.transform.scale(tile_img, (TILE_SIZE, TILE_SIZE))

        # Define a imagem do tile.
        self.image = tile_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Posiciona o tile
        self.rect.x = TILE_SIZE * column
        self.rect.y = TILE_SIZE * row


# Classe Jogador que representa o herói
class Player(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, player_img, row, column, blocks):

        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Define estado atual
        # Usamos o estado para decidir se o jogador pode ou não pular
        self.state = STILL

        # Ajusta o tamanho da imagem
        player_img = pygame.transform.scale(player_img, (PLAYER_WIDTH, PLAYER_HEIGHT))

        # Define a imagem do sprite. Nesse exemplo vamos usar uma imagem estática (não teremos animação durante o pulo)
        self.image = player_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Guarda o grupo de blocos para tratar as colisões
        self.blocks = blocks

        # Posiciona o personagem
        # row é o índice da linha embaixo do personagem
        self.rect.x = column * TILE_SIZE
        self.rect.bottom = row * TILE_SIZE

        self.speedx = 0
        self.speedy = 0

    # Metodo que atualiza a posição do personagem
    def update(self):
        # Vamos tratar os movimentos de maneira independente.
        # Primeiro tentamos andar no eixo y e depois no x.

        # Tenta andar em y
        # Atualiza a velocidade aplicando a aceleração da gravidade
        self.speedy += GRAVITY
        # Atualiza o estado para caindo
        if self.speedy > 0:
            self.state = FALLING
        # Atualiza a posição y
        self.rect.y += self.speedy
        # Se colidiu com algum bloco, volta para o ponto antes da colisão
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions:
            # Estava indo para baixo
            if self.speedy > 0:
                self.rect.bottom = collision.rect.top
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL
            # Estava indo para cima
            elif self.speedy < 0:
                self.rect.top = collision.rect.bottom
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL

        # Tenta andar em x
        self.rect.x += self.speedx
        # Corrige a posição caso tenha passado do tamanho da janela
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right >= WIDTH:
            self.rect.right = WIDTH - 1
        # Se colidiu com algum bloco, volta para o ponto antes da colisão
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions:
            # Estava indo para a direita
            if self.speedx > 0:
                self.rect.right = collision.rect.left
            # Estava indo para a esquerda
            elif self.speedx < 0:
                self.rect.left = collision.rect.right

    # Método que faz o personagem pular
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING


# Carrega todos os assets de uma vez.
def load_assets(img_dir):
    assets = {}
    assets[PLAYER_IMG] = pygame.image.load(path.join(img_dir, 'hero-single.png')).convert_alpha()
    assets[BLOCK] = pygame.image.load(path.join(img_dir, 'tile-block.png')).convert()
    return assets


def game_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega assets
    assets = load_assets(img_dir)

    # Cria um grupo de todos os sprites.
    all_sprites = pygame.sprite.Group()
    # Cria um grupo somente com os sprites de bloco.
    # Sprites de block são aqueles que impedem o movimento do jogador
    blocks = pygame.sprite.Group()

    # Cria Sprite do jogador
    player = Player(assets[PLAYER_IMG], 12, 2, blocks)

    # Cria tiles de acordo com o mapa
    for row in range(len(MAP)):
        for column in range(len(MAP[row])):
            tile_type = MAP[row][column]
            if tile_type == BLOCK:
                tile = Tile(assets[tile_type], row, column)
                all_sprites.add(tile)
                blocks.add(tile)

    # Adiciona o jogador no grupo de sprites por último para ser desenhado por
    # cima dos blocos
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

            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_LEFT:
                    player.speedx -= SPEED_X
                elif event.key == pygame.K_RIGHT:
                    player.speedx += SPEED_X
                elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    player.jump()

            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_LEFT:
                    player.speedx += SPEED_X
                elif event.key == pygame.K_RIGHT:
                    player.speedx -= SPEED_X

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
print('Utilize as setas do teclado para andar e pular.')

# Comando para evitar travamentos.
try:
    game_screen(screen)
finally:
    pygame.quit()
