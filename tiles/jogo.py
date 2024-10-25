# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
from constantes import *


# Classe Tile que representa um quadrado do mapa
class Tile(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, tile_img, row, column):
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Define a imagem do tile.
        self.image = tile_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Posiciona o tile
        self.rect.x = TILE_SIZE * column
        self.rect.y = TILE_SIZE * row


def inicializa():
    pygame.init()

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITULO)

    # Cada tile é uma imagem quadrada de TILE_SIZE x TILE_SIZE pixels.
    assets = {
        GRASS: pygame.transform.scale(pygame.image.load(IMG_DIR / 'tile-grass.png'), (TILE_SIZE, TILE_SIZE)),
        SAND1: pygame.transform.scale(pygame.image.load(IMG_DIR / 'tile-sand1.png'), (TILE_SIZE, TILE_SIZE)),
        SAND2: pygame.transform.scale(pygame.image.load(IMG_DIR / 'tile-sand2.png'), (TILE_SIZE, TILE_SIZE)),
        SAND3: pygame.transform.scale(pygame.image.load(IMG_DIR / 'tile-sand3.png'), (TILE_SIZE, TILE_SIZE)),
        SAND4: pygame.transform.scale(pygame.image.load(IMG_DIR / 'tile-sand4.png'), (TILE_SIZE, TILE_SIZE)),
        SAND5: pygame.transform.scale(pygame.image.load(IMG_DIR / 'tile-sand5.png'), (TILE_SIZE, TILE_SIZE)),
        SAND6: pygame.transform.scale(pygame.image.load(IMG_DIR / 'tile-sand6.png'), (TILE_SIZE, TILE_SIZE)),
        SAND7: pygame.transform.scale(pygame.image.load(IMG_DIR / 'tile-sand7.png'), (TILE_SIZE, TILE_SIZE)),
        SAND8: pygame.transform.scale(pygame.image.load(IMG_DIR / 'tile-sand8.png'), (TILE_SIZE, TILE_SIZE)),
        WATER: pygame.transform.scale(pygame.image.load(IMG_DIR / 'tile-water.png'), (TILE_SIZE, TILE_SIZE)),
    }
    # Cria um grupo de tiles.
    tile_map = pygame.sprite.Group()
    # Cria tiles de acordo com o mapa
    for row in range(len(MAP)):
        for column in range(len(MAP[row])):
            tile_type = MAP[row][column]
            tile = Tile(assets[tile_type], row, column)
            tile_map.add(tile)
    assets['tile_map'] = tile_map

    return window, assets


def atualiza_estado():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def game_loop(window, assets):
    while atualiza_estado():
        desenha(window, assets)


def desenha(window, assets):
    # A cada frame, redesenha o fundo e os sprites
    window.fill(BLACK)
    assets['tile_map'].draw(window)

    pygame.display.update()


if __name__ == '__main__':
    window, assets = inicializa()
    game_loop(window, assets)
