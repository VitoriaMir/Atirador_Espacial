import pygame
import sys
import random

pygame.init()

largura_tela = 800
altura_tela = 600
cor_fundo = (0, 0, 0)

nave_largura = 50
nave_altura = 50
nave_cor = (0, 255, 0)
nave_velocidade = 20

obstaculo_largura = 50
obstaculo_altura = 50
obstaculo_cor = (255, 0, 0)
obstaculo_velocidade = 5

tiro_largura = 5
tiro_altura = 10
tiro_cor = (255, 255, 0)
tiro_velocidade = 15


def desenhar_nave(tela, x, y):
    pygame.draw.rect(tela, nave_cor, [x, y, nave_largura, nave_altura])


def desenhar_obstaculo(tela, x, y):
    pygame.draw.rect(tela, obstaculo_cor, [x, y, obstaculo_largura, obstaculo_altura])


def desenhar_tiro(tela, x, y):
    pygame.draw.rect(tela, tiro_cor, [x, y, tiro_largura, tiro_altura])


def jogo():
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("Atirador Espacial")
    icone = pygame.image.load("icon.png")

    nave_x = largura_tela // 2 - nave_largura // 2
    nave_y = altura_tela - nave_altura - 10

    obstaculo_x = random.randint(0, largura_tela - obstaculo_largura)
    obstaculo_y = -obstaculo_altura

    tiros = []

    clock = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                    nave_x -= nave_velocidade
                elif evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                    nave_x += nave_velocidade
                elif evento.key == pygame.K_SPACE or evento.key == pygame.K_UP:
                    tiros.append([nave_x + nave_largura // 2 - tiro_largura // 2, nave_y])

        obstaculo_y += obstaculo_velocidade

        for tiro in tiros:
            tiro[1] -= tiro_velocidade

        if (
                nave_x < obstaculo_x + obstaculo_largura
                and nave_x + nave_largura > obstaculo_x
                and nave_y < obstaculo_y + obstaculo_altura
                and nave_y + nave_altura > obstaculo_y
        ):
            print("Game Over!")
            pygame.quit()
            sys.exit()

        tela.fill(cor_fundo)
        pygame.display.set_icon(icone)
        desenhar_nave(tela, nave_x, nave_y)
        desenhar_obstaculo(tela, obstaculo_x, obstaculo_y)

        for tiro in tiros:
            desenhar_tiro(tela, tiro[0], tiro[1])

        if obstaculo_y > altura_tela:
            obstaculo_x = random.randint(0, largura_tela - obstaculo_largura)
            obstaculo_y = -obstaculo_altura

        pygame.display.flip()
        clock.tick(60)


jogo()
