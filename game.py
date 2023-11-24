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

# game = True
# clock = pygame.time.Clock()
# jogador = Dinossauro([mergulho, correndo, pulando], all_sprites, all_bullets, bullet_img)

for i in range(4):
    nuvem = Nuvem(nuvens_img)
    all_sprites.add(nuvem)

mortes = 0

def jogo():
    game = True
    clock = pygame.time.Clock()
    jogador = Dinossauro([mergulho, correndo, pulando], all_sprites, all_bullets, bullet_img)
    mortes = 0
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
            if jogador.rect.colliderect(obstaculo.rect):
                pygame.time.delay(2000)
                mortes += 1
                game_over(mortes)

        fundo_tela()
        
        ponto()

        pygame.display.update()

def game_over(mortes):
    global pontos
    game = True
    mortes = 0

    while game:
        window.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if mortes == 0:
            mensagem = font.render("Clique em qualquer tecla para começar", True, (0, 0, 0))
        elif mortes > 0:
            mensagem = font.render("Clique em qualquer tecla para reiniciar", True, (0, 0, 0))
            pontos_obtidos = font.render("Sua pontuação: " + str(pontos), True, (0, 0, 0))
            pontos_rect = pontos_obtidos.get_rect()
            pontos_rect.center = (WIDTH // 2, HEIGHT // 2 + 50)
            window.blit(pontos_obtidos, pontos_rect)
        mensagem_rect = mensagem.get_rect()
        mensagem_rect.center = (WIDTH // 2, HEIGHT // 2)
        window.blit(mensagem, mensagem_rect)
        window.blit(correndo[0], (WIDTH // 2 - 20, HEIGHT // 2 - 140))
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game = False
            if evento.type == pygame.KEYDOWN:
                jogo()

game_over(mortes=0)