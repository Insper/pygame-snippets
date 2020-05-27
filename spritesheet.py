# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
import random
import time
from os import path

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'img')

# Dados gerais do jogo.
TITULO = 'Exemplo de Sprite Sheets e Animações'
WIDTH = 480 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define estados possíveis do jogador
STILL = 0
WALKING = 1
JUMPING = 2
FIGHTING = 3
SWIMMING = 4


# Recebe uma imagem de sprite sheet e retorna uma lista de imagens. 
# É necessário definir quantos sprites estão presentes em cada linha e coluna.
# Essa função assume que os sprites no sprite sheet possuem todos o mesmo tamanho.
def load_spritesheet(spritesheet, rows, columns):
    # Calcula a largura e altura de cada sprite.
    sprite_width = spritesheet.get_width() // columns
    sprite_height = spritesheet.get_height() // rows
    
    # Percorre todos os sprites adicionando em uma lista.
    sprites = []
    for row in range(rows):
        for column in range(columns):
            # Calcula posição do sprite atual
            x = column * sprite_width
            y = row * sprite_height
            # Define o retângulo que contém o sprite atual
            dest_rect = pygame.Rect(x, y, sprite_width, sprite_height)

            # Cria uma imagem vazia do tamanho do sprite
            image = pygame.Surface((sprite_width, sprite_height), pygame.SRCALPHA)
            # Copia o sprite atual (do spritesheet) na imagem
            image.blit(spritesheet, (0, 0), dest_rect)
            sprites.append(image)
    return sprites


# Classe Jogador que representa o herói
class Player(pygame.sprite.Sprite):
    
    # Construtor da classe. O argumento player_sheet é uma imagem contendo um spritesheet.
    def __init__(self, player_sheet):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Aumenta o tamanho do spritesheet para ficar mais fácil de ver
        player_sheet = pygame.transform.scale(player_sheet, (640, 640))

        # Define sequências de sprites de cada animação
        spritesheet = load_spritesheet(player_sheet, 4, 4)
        self.animations = {
            STILL: spritesheet[0:4],
            WALKING: spritesheet[4:7],
            JUMPING: spritesheet[7:8],
            FIGHTING: spritesheet[8:12],
            SWIMMING: spritesheet[12:16],
        }
        # Define estado atual (que define qual animação deve ser mostrada)
        self.state = STILL
        # Define animação atual
        self.animation = self.animations[self.state]
        # Inicializa o primeiro quadro da animação
        self.frame = 0
        self.image = self.animation[self.frame]
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza na tela.
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2

        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 300
        
    # Metodo que atualiza a posição do personagem
    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()

        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:

            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Atualiza animação atual
            self.animation = self.animations[self.state]
            # Reinicia a animação caso o índice da imagem atual seja inválido
            if self.frame >= len(self.animation):
                self.frame = 0
            
            # Armazena a posição do centro da imagem
            center = self.rect.center
            # Atualiza imagem atual
            self.image = self.animation[self.frame]
            # Atualiza os detalhes de posicionamento
            self.rect = self.image.get_rect()
            self.rect.center = center
    

def game_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega spritesheet
    player_sheet = pygame.image.load(path.join(img_dir, 'hero.png')).convert_alpha()

    # Cria Sprite do jogador
    player = Player(player_sheet)
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
            
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_1:
                    player.state = STILL
                elif event.key == pygame.K_2:
                    player.state = WALKING
                elif event.key == pygame.K_3:
                    player.state = JUMPING
                elif event.key == pygame.K_4:
                    player.state = FIGHTING
                elif event.key == pygame.K_5:
                    player.state = SWIMMING
                
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
print('Utilize as teclas "1", "2", "3", "4" e "5" do seu teclado para mudar a animação atual.')

# Comando para evitar travamentos.
try:
    game_screen(screen)
finally:
    pygame.quit()
