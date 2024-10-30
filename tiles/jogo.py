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
        self.rect.x = TAMANHO_QUADRADO * column
        self.rect.y = TAMANHO_QUADRADO * row


def inicializa():
    pygame.init()

    janela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption(TITULO)

    # Cada tile é uma imagem quadrada de TILE_SIZE x TILE_SIZE pixels.
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
    }
    # Cria um grupo de tiles.
    mapa_tiles = pygame.sprite.Group()
    # Cria tiles de acordo com o mapa
    for linha in range(len(MAPA)):
        for coluna in range(len(MAPA[linha])):
            tipo_quadrado = MAPA[linha][coluna]
            quadrado = Tile(assets[tipo_quadrado], linha, coluna)
            mapa_tiles.add(quadrado)
    assets['mapa_tiles'] = mapa_tiles

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
    assets['mapa_tiles'].draw(janela)

    pygame.display.update()


if __name__ == '__main__':
    janela, assets = inicializa()
    game_loop(janela, assets)
