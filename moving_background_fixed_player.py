# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
import random
from os import path

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'img')

# Dados gerais do jogo.
TITULO = 'Exemplo de Fundo em Movimento'
WIDTH = 1024 # Largura da tela
HEIGHT = 768 # Altura da tela
FPS = 60 # Frames por segundo
PLAYER_IMG = 'player_img'
BLOCK_IMG = 'block_img'
BACKGROUND_IMG = 'background_img'

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Outras constantes
INITIAL_BLOCKS = 6
TILE_SIZE = 80
SPEED_X = 10


# Class que representa os blocos do cenário
class Tile(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, tile_img, x, y):
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Aumenta o tamanho do tile.
        tile_img = pygame.transform.scale(tile_img, (TILE_SIZE, TILE_SIZE))

        # Define a imagem do tile.
        self.image = tile_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Posiciona o tile
        self.rect.x = x
        self.rect.y = y

        self.speedx = 0

    def update(self):
        self.rect.x += self.speedx


# Classe Jogador que representa o herói
class Player(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, player_img):

        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Aumenta o tamanho da imagem
        player_img = pygame.transform.scale(player_img, (100, 160))

        # Define a imagem do sprite. Nesse exemplo vamos usar uma imagem estática (não teremos animação durante o pulo)
        self.image = player_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Começa no centro da janela
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = int(HEIGHT * 7 / 8)

        # O jogador não vai se mover, mas guardamos essa informação para o
        # fundo e os objetos do mundo se moverem no sentido oposto.
        self.speedx = 0


# Carrega todos os assets de uma vez.
def load_assets(img_dir):
    assets = {}
    assets[PLAYER_IMG] = pygame.image.load(path.join(img_dir, 'hero-single.png')).convert_alpha()
    assets[BLOCK_IMG] = pygame.image.load(path.join(img_dir, 'tile-block.png')).convert()
    assets[BACKGROUND_IMG] = pygame.image.load(path.join(img_dir, 'background.png')).convert()
    return assets


def game_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega assets
    assets = load_assets(img_dir)

    # Carrega o fundo do jogo
    background = assets[BACKGROUND_IMG]
    # Redimensiona o fundo
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    # Cria Sprite do jogador
    player = Player(assets[PLAYER_IMG])
    # Cria um grupo de todos os sprites e adiciona o jogador.
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    # Cria um grupo para guardar somente os sprites do mundo (obstáculos, objetos, etc).
    # Esses sprites vão andar junto com o mundo (fundo)
    world_sprites = pygame.sprite.Group()
    # Cria blocos espalhados em posições aleatórias do mapa
    for i in range(INITIAL_BLOCKS):
        block_x = random.randint(0, WIDTH)
        block_y = random.randint(0, int(HEIGHT * 0.5))
        block = Tile(assets[BLOCK_IMG], block_x, block_y)
        world_sprites.add(block)
        # Adiciona também no grupo de todos os sprites para serem atualizados e desenhados
        all_sprites.add(block)

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

            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_LEFT:
                    player.speedx += SPEED_X
                elif event.key == pygame.K_RIGHT:
                    player.speedx -= SPEED_X

        # Depois de processar os eventos.
        # Como o jogador vai ficar parado, o fundo e os objetos no mundo devem
        # se mover com a velocidade do personagem no sentido oposto.
        for block in world_sprites:
            block.speedx = -player.speedx

        # Atualiza a acao de cada sprite. O grupo chama o método update() de cada Sprite dentre dele.
        all_sprites.update()

        # Atualiza a posição da imagem de fundo.
        background_rect.x -= player.speedx
        # Se o fundo saiu da janela, faz ele voltar para dentro.
        # Verifica se o fundo saiu para a esquerda
        if background_rect.right < 0:
            background_rect.x += background_rect.width
        # Verifica se o fundo saiu para a direita
        if background_rect.left >= WIDTH:
            background_rect.x -= background_rect.width

        # Verifica se algum bloco saiu da janela
        for block in world_sprites:
            if block.rect.right < 0:
                # Destrói o bloco e cria um novo no final da tela
                block.kill()
                block_x = random.randint(WIDTH, int(WIDTH * 1.5))
                block_y = random.randint(0, int(HEIGHT * 0.5))
                new_block = Tile(assets[BLOCK_IMG], block_x, block_y)
                all_sprites.add(new_block)
                world_sprites.add(new_block)

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)

        # Desenha o fundo e uma cópia para a direita.
        # Assumimos que a imagem selecionada ocupa pelo menos o tamanho da janela.
        # Além disso, ela deve ser cíclica, ou seja, o lado esquerdo deve ser continuação do direito.
        screen.blit(background, background_rect)
        # Desenhamos a imagem novamente, mas deslocada em x.
        background_rect2 = background_rect.copy()
        if background_rect.left > 0:
            # Precisamos desenhar o fundo à esquerda
            background_rect2.x -= background_rect2.width
        else:
            # Precisamos desenhar o fundo à direita
            background_rect2.x += background_rect2.width
        screen.blit(background, background_rect2)

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
print('Este exemplo não é interativo.')

# Comando para evitar travamentos.
try:
    game_screen(screen)
finally:
    pygame.quit()
