import pygame
from constantes import *


# Classe Jogador que representa o herói
class Jogador(pygame.sprite.Sprite):
    def __init__(self, jogador_img):
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Define estado atual
        # Usamos o estado para decidir se o jogador pode ou não pular
        self.estado = PARADO

        # Aumenta o tamanho da imagem para ficar mais fácil de ver
        jogador_img = pygame.transform.scale(jogador_img, (100, 160))

        # Define a imagem do sprite. Nesse exemplo vamos usar uma imagem estática (não teremos animação durante o pulo)
        self.image = jogador_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Começa no topo da janela e cai até o chão
        self.rect.centerx = LARGURA / 2
        self.rect.top = 0

        self.velocidade_y = 0

    # Metodo que atualiza a posição do personagem
    def update(self, dt):
        self.velocidade_y += GRAVIDADE * dt
        # Atualiza o estado para caindo
        if self.velocidade_y > 0:
            self.estado = CAINDO
        self.rect.y += self.velocidade_y * dt
        # Se bater no chão, para de cair
        if self.rect.bottom >= CHAO:
            # Reposiciona para a posição do chão
            self.rect.bottom = CHAO
            # Para de cair
            self.velocidade_y = 0
            # Atualiza o estado para parado
            self.estado = PARADO

    # Método que faz o personagem pular
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.estado == PARADO:
            self.velocidade_y -= VELOCIDADE_PULO
            self.estado = PULANDO


def inicializa():
    pygame.init()

    window = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption(TITULO)

    # Imprime instruções
    print('*' * len(TITULO))
    print(TITULO.upper())
    print('*' * len(TITULO))
    print('Utilize a tecla "ESPAÇO" ou seta para cima para pular.')

    # Carrega imagem
    jogador_img = pygame.image.load(IMG_DIR / 'hero-single.png').convert_alpha()

    # Cria Sprite do jogador
    jogador = Jogador(jogador_img)
    # Cria um grupo de todos os sprites e adiciona o jogador.
    todos_sprites = pygame.sprite.Group()
    todos_sprites.add(jogador)

    estado = {
        'jogador': jogador,
        'todos_sprites': todos_sprites,
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
                estado['jogador'].jump()

    # Depois de processar os eventos.
    # Atualiza a acao de cada sprite. O grupo chama o método update() de cada Sprite dentre dele.
    estado['todos_sprites'].update(dt)

    return True


def desenha(window, estado):
    window.fill(PRETO)
    # Desenha chão
    pygame.draw.rect(window, VERDE, (0, CHAO, LARGURA, ALTURA - CHAO))
    estado['todos_sprites'].draw(window)

    pygame.display.update()


def game_loop(window, estado):
    while atualiza_estado(estado):
        desenha(window, estado)


if __name__ == '__main__':
    window, estado = inicializa()
    game_loop(window, estado)
