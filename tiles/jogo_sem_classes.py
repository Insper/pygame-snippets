# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
from constantes import *


def inicializa():
    pygame.init()

    janela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption(TITULO)

    # Cada tile é uma imagem quadrada de TAMANHO_QUADRADO x TAMANHO_QUADRADO pixels.
    assets = {
        GRAMA_: pygame.transform.scale(pygame.image.load(IMG_DIR / 'tile-grass.png'), (TAMANHO_QUADRADO, TAMANHO_QUADRADO)),
        AREIA1: pygame.transform.scale(pygame.image.load(IMG_DIR / 'tile-sand1.png'), (TAMANHO_QUADRADO, TAMANHO_QUADRADO)),
        AREIA2: pygame.transform.scale(pygame.image.load(IMG_DIR / 'tile-sand2.png'), (TAMANHO_QUADRADO, TAMANHO_QUADRADO)),
        AREIA3: pygame.transform.scale(pygame.image.load(IMG_DIR / 'tile-sand3.png'), (TAMANHO_QUADRADO, TAMANHO_QUADRADO)),
        AREIA4: pygame.transform.scale(pygame.image.load(IMG_DIR / 'tile-sand4.png'), (TAMANHO_QUADRADO, TAMANHO_QUADRADO)),
        AREIA5: pygame.transform.scale(pygame.image.load(IMG_DIR / 'tile-sand5.png'), (TAMANHO_QUADRADO, TAMANHO_QUADRADO)),
        AREIA6: pygame.transform.scale(pygame.image.load(IMG_DIR / 'tile-sand6.png'), (TAMANHO_QUADRADO, TAMANHO_QUADRADO)),
        AREIA7: pygame.transform.scale(pygame.image.load(IMG_DIR / 'tile-sand7.png'), (TAMANHO_QUADRADO, TAMANHO_QUADRADO)),
        AREIA8: pygame.transform.scale(pygame.image.load(IMG_DIR / 'tile-sand8.png'), (TAMANHO_QUADRADO, TAMANHO_QUADRADO)),
        AGUA__: pygame.transform.scale(pygame.image.load(IMG_DIR / 'tile-water.png'), (TAMANHO_QUADRADO, TAMANHO_QUADRADO)),
        'mapa_tiles': MAPA,
    }

    return janela, assets


def atualiza_estado():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def game_loop(janela, assets):
    while atualiza_estado():
        desenha(janela, assets)


def desenha(janela, assets):
    # A cada frame, redesenha o fundo e os sprites
    janela.fill(PRETO)

    for linha in range(len(assets['mapa_tiles'])):
        for coluna in range(len(assets['mapa_tiles'][linha])):
            tipo_quadrado = assets['mapa_tiles'][linha][coluna]
            janela.blit(assets[tipo_quadrado], (TAMANHO_QUADRADO * coluna, TAMANHO_QUADRADO * linha))

    pygame.display.update()


if __name__ == '__main__':
    janela, assets = inicializa()
    game_loop(janela, assets)
