# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
from os import path

# Dados gerais do jogo.
TITULO = 'Exemplo de Menu de Texto'
WIDTH = 600 # Largura da tela
HEIGHT = 200 # Altura da tela
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define a sequência de textos
MENUS = {
    'Principal': ['Menu 1', 'Menu 2', 'Sair'],
    'Menu 1': ['Principal', 'Menu 2', 'Sair'],
    'Menu 2': ['Principal', 'Menu 1', 'Sair'],
    'Sair': [],
}

def game_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega a fonte padrão do sistema
    font = pygame.font.SysFont(None, 16)

    # Vamos utilizar esta variável para controlar o texto a ser mostrado
    text_index = 0
    game = True
    menu_atual = 'Principal'
    item_atual = 0
    while menu_atual != 'Sair' and game:
        menu = MENUS[menu_atual]
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():

            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                game = False

            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    menu_atual = menu[item_atual]
                if event.key == pygame.K_UP:
                    item_atual -= 1
                    if item_atual < 0:
                        item_atual = 0
                if event.key == pygame.K_DOWN:
                    item_atual += 1
                    if item_atual >= len(menu):
                        item_atual = len(menu) - 1

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)

        # Desenha os textos na tela
        # Desenha o título do menu
        text_image = font.render(menu_atual, True, WHITE)
        screen.blit(text_image, (10, 10))
        for i in range(len(menu)):
            text = menu[i]
            if i == item_atual:
                text = '> ' + text
            else:
                text = '  ' + text
            text_image = font.render(text, True, WHITE)
            screen.blit(text_image, (10, 10 + (i + 1) * 16))

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
print('Aperte a tecla espaço para avançar para o próximo texto.')

# Comando para evitar travamentos.
try:
    game_screen(screen)
finally:
    pygame.quit()
