# Exemplos de Código em PyGame

## Construindo mapas com tiles

*Tiles* permitem a construção de mapas através do nosso código. Ao invés de termos uma grande imagem para o fundo podemos construir um mapa a partir de unidades menores (os *tiles*). Isso nos dá algumas vantagens:

- Flexibilização dos mapas: podemos construir quantos mapas quisermos sem ter que gerar uma imagem diferente para cada um;
- Controle de colisão: podemos tratar alguns tiles de maneira especial fazendo um tratamento de colisão. Alguns exemplos:
    - Podemos impedir que o jogador passe por aquele ponto, criando tiles de parede ou chão, por exemplo (TO DO);
    - Podemos criar tipos de terrenos distintos (verificamos quais tiles colidiram com o jogador e assim modificamos sua velocidade);
- Mapa em camadas: podemos desenhar um tile sobre o outro, por exemplo, com um tile de arbusto sobre um tile de terra. Assim, quando o jogador corta o arbusto ele some, mas o de terra permanece.
- As possibilidades são infinitas, use sua criatividade!

## Fazendo o personagem pular

Vamos apresentar alguns exemplos de como fazer o personagem pular ao apertarmos a tecla `ESPAÇO`. No primeiro exemplo ([jump.py](jump.py)) temos uma versão simplificada, assumindo que o chão está fixo em uma determinada altura.



## Alternando animações com sprite sheets

Um sprite sheet é uma imagem que é composta por diversos sprites do nosso jogo. É comum utilizarmos sprite sheets para armazenar sequências de quadros de uma animação. Um exemplo é a imagem a seguir:

![Sprite sheet de um personagem]()

Podemos dividir esse sprite sheet em 5 animações: personagem parado (primeira linha), personagem correndo (1a a 3a imagens da segunda linha), personagem pulando (4a imagem da segunda linha), personagem lutando (terceira linha) e personagem nadando (quarta linha).

No arquivo [spritesheet.py](spritesheet.py) mostramos como usar um sprite sheet para animar um personagem dependendo do seu estado atual.

# Referências

- [`hero.png`](img/hero.png): [https://opengameart.org/content/classic-hero](https://opengameart.org/content/classic-hero)
- [`32x32_map_tile v3.1 [MARGINLESS].png`](img/32x32_map_tile v3.1 [MARGINLESS].png): [https://opengameart.org/content/basic-map-32x32-by-silver-iv](https://opengameart.org/content/basic-map-32x32-by-silver-iv)