# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
import math
from os import path

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'img')

# Cores
BLACK = (0, 0, 0)

# Dados gerais do jogo.
TITULO = 'Exemplo de Rotação com o Mouse'
WIDTH = 600 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 60 # Frames por segundo


# Classe Jogador que representa o herói
class Player(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, player_img):

        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Define a imagem do sprite. Nesse exemplo vamos usar uma imagem estática (não teremos animação durante o pulo)
        self.image = player_img
        # Criamos uma cópia da imagem original. Essa imagem será rotacionada a cada frame
        self.orig_image = player_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Personagem fica sempre no meio da tela
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2

    # Metodo que atualiza a posição do personagem
    def update(self):
        # Pega a posição do mouse
        mouse = pygame.mouse.get_pos()
        mouse_x = mouse[0]
        mouse_y = mouse[1]

        # Guarda a posição do jogador em variáveis para facilitar
        cx = self.rect.centerx
        cy = self.rect.centery

        # Calcula o vetor do centro do personagem até o mouse
        direcao_x = mouse_x - cx
        direcao_y = mouse_y - cy

        # Calcula o ângulo entre o eixo horizontal e o vetor da direção
        angulo_radianos = math.atan2(direcao_y, direcao_x)
        angulo_graus = math.degrees(angulo_radianos)

        # Rotaciona a imagem
        # Como a imagem da nave está inicialmente apontando para cima, devemos
        # somar 90 graus, pois angulo_graus é contado a partir do eixo x positivo.
        # Nesse caso, o eixo x positivo seria a nave apontando para a direita.
        # Além disso, o eixo y aponta para baixo, mas a função math.atan2 assume
        # que o y aponta para cima, por isso devemos inverter a direção do ângulo
        angulo_rotacao = -(angulo_graus + 90)
        self.image = pygame.transform.rotate(self.orig_image, angulo_rotacao)
        self.rect = self.image.get_rect()
        self.rect.centerx = cx
        self.rect.centery = cy


def game_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega imagem
    player_img = pygame.image.load(path.join(img_dir, 'player-top.png')).convert_alpha()

    # Cria Sprite do jogador
    player = Player(player_img)
    # Cria um grupo de todos os sprites e adiciona o jogador.
    all_sprites = pygame.sprite.Group()
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
print('Mova o mouse para girar o personagem.')

# Comando para evitar travamentos.
try:
    game_screen(screen)
finally:
    pygame.quit()
