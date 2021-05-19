# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
from os import path

# Dados gerais do jogo.
TITULO = 'Exemplo de Animação de Texto'
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
TEXT_STATES = [
    'Este texto aparecerá aos poucos [aperte espaço para continuar]',
    'Você pode colocar quantos você quiser [aperte espaço para continuar]',
    'E inclusive alternar entre textos e outros tipos de estado [aperte espaço para continuar]',
    'Este é o último passo. A janela vai fechar depois que você apertar espaço.',
]

def game_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega a fonte padrão do sistema
    font = pygame.font.SysFont(None, 16)

    # Vamos utilizar esta variável para controlar o texto a ser mostrado
    text_index = 0
    game = True
    while text_index < len(TEXT_STATES) and game:

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
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    text_index += 1

        # Depois de processar os eventos.
        # Atualiza o texto a ser mostrado na tela
        if text_index < len(TEXT_STATES):
            text = TEXT_STATES[text_index]
        else:
            text = ''
        text_image = font.render(text, True, WHITE)

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(text_image, (10, 10))

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
