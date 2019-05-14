# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
import random
from os import path

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'img')

# Dados gerais do jogo.
TITULO = 'Exemplo de Tiles'
WIDTH = 480 # Largura da tela
HEIGHT = 600 # Altura da tela
TILE_SIZE = 40 # Tamanho de cada tile (cada tile é um quadrado)
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define os tipos de tiles
GRASS = 0
SAND1 = 1
SAND2 = 2
SAND3 = 3
SAND4 = 4
SAND5 = 5
SAND6 = 6
SAND7 = 7
SAND8 = 8
WATER = 9

# Define o mapa com os tipos de tiles
MAP = [
    [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
    [GRASS, SAND1, SAND2, SAND2, SAND3, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
    [GRASS, SAND4, WATER, WATER, SAND5, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
    [GRASS, SAND4, WATER, WATER, SAND5, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
    [GRASS, SAND4, WATER, WATER, SAND5, GRASS, SAND1, SAND2, SAND2, SAND3, GRASS, GRASS],
    [GRASS, SAND4, WATER, WATER, SAND5, GRASS, SAND4, WATER, WATER, SAND5, GRASS, GRASS],
    [GRASS, SAND6, SAND7, SAND7, SAND8, GRASS, SAND4, WATER, WATER, SAND5, GRASS, GRASS],
    [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, SAND4, WATER, WATER, SAND5, GRASS, GRASS],
    [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, SAND4, WATER, WATER, SAND5, GRASS, GRASS],
    [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, SAND4, WATER, WATER, SAND5, GRASS, GRASS],
    [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, SAND4, WATER, WATER, SAND5, GRASS, GRASS],
    [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, SAND4, WATER, WATER, SAND5, GRASS, GRASS],
    [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, SAND4, WATER, WATER, SAND5, GRASS, GRASS],
    [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, SAND6, SAND7, SAND7, SAND8, GRASS, GRASS],
    [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
]

# Define estados possíveis do jogador
STILL = 0
JUMPING = 1
FALLING = 2

# Classe Jogador que representa o herói
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


# Carrega todos os assets de uma vez.
def load_assets(img_dir):
    assets = {}
    assets[GRASS] = pygame.image.load(path.join(img_dir, 'tile-grass.png')).convert()
    assets[SAND1] = pygame.image.load(path.join(img_dir, 'tile-sand1.png')).convert()
    assets[SAND2] = pygame.image.load(path.join(img_dir, 'tile-sand2.png')).convert()
    assets[SAND3] = pygame.image.load(path.join(img_dir, 'tile-sand3.png')).convert()
    assets[SAND4] = pygame.image.load(path.join(img_dir, 'tile-sand4.png')).convert()
    assets[SAND5] = pygame.image.load(path.join(img_dir, 'tile-sand5.png')).convert()
    assets[SAND6] = pygame.image.load(path.join(img_dir, 'tile-sand6.png')).convert()
    assets[SAND7] = pygame.image.load(path.join(img_dir, 'tile-sand7.png')).convert()
    assets[SAND8] = pygame.image.load(path.join(img_dir, 'tile-sand8.png')).convert()
    assets[WATER] = pygame.image.load(path.join(img_dir, 'tile-water.png')).convert()
    return assets


def game_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega assets
    assets = load_assets(img_dir)

    # Cria um grupo de tiles.
    tiles = pygame.sprite.Group()
    # Cria tiles de acordo com o mapa
    for row in range(len(MAP)):
        for column in range(len(MAP[row])):
            tile_type = MAP[row][column]
            tile = Tile(assets[tile_type], row, column)
            tiles.add(tile)

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

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        tiles.draw(screen)

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
print('Este exemplo não é interativo.')

# Comando para evitar travamentos.
try:
    game_screen(screen)
finally:
    pygame.quit()
