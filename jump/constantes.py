from pathlib import Path

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = Path(__file__).parent.parent / 'img'

# Dados gerais do jogo.
TITULO = 'Exemplo de Pulo'
LARGURA = 480 # Largura da tela
ALTURA = 600 # Altura da tela
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)

# Define a aceleração da gravidade
GRAVIDADE = 1000  # px / s^2
# Define a velocidade inicial no pulo
VELOCIDADE_PULO = 500  # px / s
# Define a altura do chão
CHAO = ALTURA * 5 // 6

# Define estados possíveis do jogador
PARADO = 0
PULANDO = 1
CAINDO = 2
