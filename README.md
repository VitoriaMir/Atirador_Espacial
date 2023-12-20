Este é um jogo básico de atirador espacial implementado em Pygame.

## Configurações do Jogo

- **Tamanho da Tela:** 800x600 pixels
- **Cor de Fundo:** RGB(0, 0, 0)

## Configurações da Nave

- **Dimensões:** 50x50 pixels
- **Cor:** RGB(0, 255, 0)
- **Velocidade:** 20 pixels por frame

## Configurações do Obstáculo

- **Dimensões:** 50x50 pixels
- **Cor:** RGB(255, 0, 0)
- **Velocidade:** 5 pixels por frame

## Configurações do Tiro

- **Dimensões:** 5x10 pixels
- **Cor:** RGB(255, 255, 0)
- **Velocidade:** 15 pixels por frame

## Funções de Desenho

### `desenhar_nave(tela, x, y)`

Desenha a nave na tela nas coordenadas `(x, y)`.

### `desenhar_obstaculo(tela, x, y)`

Desenha um obstáculo na tela nas coordenadas `(x, y)`.

### `desenhar_tiro(tela, x, y)`

Desenha um tiro na tela nas coordenadas `(x, y)`.

## Função Principal do Jogo

```python
def jogo():
    # Inicializa a tela e define configurações iniciais
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("Atirador Espacial")
    icone = pygame.image.load("icon.png")

    # Inicializa variáveis
    nave_x = largura_tela // 2 - nave_largura // 2
    nave_y = altura_tela - nave_altura - 10
    obstaculo_x = random.randint(0, largura_tela - obstaculo_largura)
    obstaculo_y = -obstaculo_altura
    tiros = []

    clock = pygame.time.Clock()

    while True:
        # Captura eventos, verifica colisões, atualiza posições e desenha elementos
        pygame.display.flip()
        clock.tick(60)

# Inicia o jogo
jogo()
```

## Controles do Jogador

- Setas Esquerda (←) e Direita (→): Movem a nave para os lados.
- Barra de Espaço ou Seta para Cima (↑): Dispara tiros.

## Condição de Game Over

```python
if (
    nave_x < obstaculo_x + obstaculo_largura
    and nave_x + nave_largura > obstaculo_x
    and nave_y < obstaculo_y + obstaculo_altura
    and nave_y + nave_altura > obstaculo_y
):
    print("Game Over!")
    pygame.quit()
    sys.exit()
```

Verifica se a nave colidiu com um obstáculo, encerrando o jogo em caso de colisão.

Esta documentação fornece uma visão geral do código, suas configurações e funcionalidades principais. Personalize conforme necessário para adicionar mais recursos e melhorias ao jogo.