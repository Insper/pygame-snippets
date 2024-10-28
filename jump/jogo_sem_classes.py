import pygame
from constantes import *


def inicializa():
    pygame.init()

    window = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption(TITULO)

    # Imprime instruções
    print('*' * len(TITULO))
    print(TITULO.upper())
    print('*' * len(TITULO))
    print('Utilize a tecla "ESPAÇO" ou seta para cima para pular.')

    jogador_img = pygame.image.load(IMG_DIR / 'hero-single.png').convert_alpha()
    jogador_img = pygame.transform.scale(jogador_img, (100, 160))

    estado = {
        'jogador': {
            'estado': PARADO,
            'img': jogador_img,
            'x': LARGURA / 2 - jogador_img.get_width() / 2,
            'y': 0,
            'largura': jogador_img.get_width(),
            'altura': jogador_img.get_height(),
            'velocidade_y': 0,
        },
        'clock': pygame.time.Clock(),
    }

    return window, estado


def atualiza_estado(estado):
    dt = estado['clock'].tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera o estado do jogador.
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                if estado['jogador']['estado'] == PARADO:
                    estado['jogador']['velocidade_y'] -= VELOCIDADE_PULO
                    estado['jogador']['estado'] = PULANDO

    # Depois de processar os eventos.
    # Atualiza a posição do jogador
    estado['jogador']['velocidade_y'] += GRAVIDADE * dt
    # Atualiza o estado para caindo
    if estado['jogador']['velocidade_y'] > 0:
        estado['jogador']['estado'] = CAINDO
    estado['jogador']['y'] += estado['jogador']['velocidade_y'] * dt
    # Se bater no chão, para de cair
    if estado['jogador']['y'] + estado['jogador']['altura'] >= CHAO:
        # Reposiciona para a posição do chão
        estado['jogador']['y'] = CHAO - estado['jogador']['altura']
        # Para de cair
        estado['jogador']['velocidade_y'] = 0
        # Atualiza o estado para parado
        estado['jogador']['estado'] = PARADO

    return True


def desenha(window, estado):
    window.fill(PRETO)
    # Desenha chão
    pygame.draw.rect(window, VERDE, (0, CHAO, LARGURA, ALTURA - CHAO))
    window.blit(estado['jogador']['img'], (int(estado['jogador']['x']), int(estado['jogador']['y'])))

    pygame.display.update()


def game_loop(window, estado):
    while atualiza_estado(estado):
        desenha(window, estado)


if __name__ == '__main__':
    window, estado = inicializa()
    game_loop(window, estado)
