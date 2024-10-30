from pathlib import Path


# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = Path(__file__).parent.parent / 'img'

# Dados gerais do jogo.
TITULO = 'Exemplo de Tiles'
LARGURA = 480 # Largura da tela
ALTURA = 600 # Altura da tela
TAMANHO_QUADRADO = 40 # Tamanho de cada quadrado (tile)

# Define algumas variáveis com as cores básicas
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VEMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)

# Define os tipos de tiles
# Os underscores no final são apenas para manter todas as variáveis com o mesmo tamanho.
GRAMA_ = 0
AREIA1 = 1
AREIA2 = 2
AREIA3 = 3
AREIA4 = 4
AREIA5 = 5
AREIA6 = 6
AREIA7 = 7
AREIA8 = 8
AGUA__ = 9

# Define o mapa com os tipos de tiles
MAPA = [
    [GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_],
    [GRAMA_, AREIA1, AREIA2, AREIA2, AREIA3, GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_],
    [GRAMA_, AREIA4, AGUA__, AGUA__, AREIA5, GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_],
    [GRAMA_, AREIA4, AGUA__, AGUA__, AREIA5, GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_],
    [GRAMA_, AREIA4, AGUA__, AGUA__, AREIA5, GRAMA_, AREIA1, AREIA2, AREIA2, AREIA3, GRAMA_, GRAMA_],
    [GRAMA_, AREIA4, AGUA__, AGUA__, AREIA5, GRAMA_, AREIA4, AGUA__, AGUA__, AREIA5, GRAMA_, GRAMA_],
    [GRAMA_, AREIA6, AREIA7, AREIA7, AREIA8, GRAMA_, AREIA4, AGUA__, AGUA__, AREIA5, GRAMA_, GRAMA_],
    [GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, AREIA4, AGUA__, AGUA__, AREIA5, GRAMA_, GRAMA_],
    [GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, AREIA4, AGUA__, AGUA__, AREIA5, GRAMA_, GRAMA_],
    [GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, AREIA4, AGUA__, AGUA__, AREIA5, GRAMA_, GRAMA_],
    [GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, AREIA4, AGUA__, AGUA__, AREIA5, GRAMA_, GRAMA_],
    [GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, AREIA4, AGUA__, AGUA__, AREIA5, GRAMA_, GRAMA_],
    [GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, AREIA4, AGUA__, AGUA__, AREIA5, GRAMA_, GRAMA_],
    [GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, AREIA6, AREIA7, AREIA7, AREIA8, GRAMA_, GRAMA_],
    [GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_, GRAMA_],
]
