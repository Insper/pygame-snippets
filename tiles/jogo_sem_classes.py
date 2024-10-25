# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
from constantes import *


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
        'tile_map': MAP,
    }

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

    for row in range(len(assets['tile_map'])):
        for column in range(len(assets['tile_map'][row])):
            tile_type = assets['tile_map'][row][column]
            window.blit(assets[tile_type], (TILE_SIZE * column, TILE_SIZE * row))

    pygame.display.update()


if __name__ == '__main__':
    window, assets = inicializa()
    game_loop(window, assets)
