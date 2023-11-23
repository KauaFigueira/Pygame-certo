import pygame
import os
import random
from imagens import *
from classes import *

pygame.init()

# Tela
WIDTH = 1000
HEIGHT = 500
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('T-rex running')


all_bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()


game = True
clock = pygame.time.Clock()
jogador = Dinossauro([mergulho, correndo, pulando], all_sprites, all_bullets, bullet_img)

for i in range(4):
    nuvem = Nuvem(nuvens_img)
    all_sprites.add(nuvem)


while game:
    # FPS
    clock.tick(30)
    # Trata eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            

    # ----- Gera saídas
    window.fill((255, 255, 255))  
    entrada = pygame.key.get_pressed()
    if entrada[pygame.K_SPACE]:
        jogador.shoot(entrada)


    jogador.update(entrada)

    all_sprites.update()
    all_sprites.draw(window)
    window.blit(jogador.image,(35,jogador.rect.y))

    if len(obstaculos) == 0:
        if random.randint(0, 2) == 0:
            obstaculos.append(CactusP(cactusP))
        elif random.randint(0, 2) == 1:
            obstaculos.append(CactusG(cactusG))
        elif random.randint(0, 2) == 2:
            obstaculos.append(passaros(passaro))

    for obstaculo in obstaculos:
        obstaculo.desenhar(window)
        obstaculo.update()

    fundo_tela()
    
    ponto()

    pygame.display.update()
    