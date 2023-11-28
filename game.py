import pygame
import os
import random
from imagens import *
from classes import *
from musica import *


pygame.init()

# Tela
WIDTH = 1000
HEIGHT = 500
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('T-rex running')




def jogo():
    clock = pygame.time.Clock()

    all_bullets = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    for i in range(4):
        nuvem = Nuvem(nuvens_img)
        all_sprites.add(nuvem)

    jogador = Dinossauro([mergulho, correndo, pulando], all_sprites, all_bullets, bullet_img)
    x_fundo = 0
    y_fundo = 380

    all_obstaculos = pygame.sprite.Group()

    velocidade = 14

    estado = 2
    while estado == 2:

        run.play()

        # FPS
        clock.tick(30)
        # Trata eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado = -1
                

        # ----- Gera saídas
        window.fill((255, 255, 255))  
        entrada = pygame.key.get_pressed()
        if entrada[pygame.K_SPACE]:
            jogador.shoot(entrada)
        jogador.update(entrada)


        if len(all_obstaculos) == 0:
            if random.randint(0, 2) == 0:
                o = CactusP(cactusP)
                all_obstaculos.add(o)
                all_sprites.add(o)
            elif random.randint(0, 2) == 1:
                o = CactusG(cactusG)
                all_obstaculos.add(o)
                all_sprites.add(o)
            elif random.randint(0, 2) == 2:
                o = Passaro(passaro)
                all_obstaculos.add(o)
                all_sprites.add(o)

        hits = pygame.sprite.spritecollide(jogador , all_obstaculos, False, pygame.sprite.collide_mask)
        if hits != []:
            run.stop()
            morte.play()
            pygame.time.delay(2000)
            estado = 9
        
        hits = pygame.sprite.groupcollide(all_bullets , all_obstaculos, True, pygame.sprite.collide_mask)
        
        WIDTH_F = cenario.get_width()
        window.blit(cenario , (x_fundo , y_fundo))
        window.blit(cenario , (WIDTH_F + x_fundo , y_fundo))
        if x_fundo <= -WIDTH_F:
            window.blit(cenario , (WIDTH_F + x_fundo , y_fundo))
            x_fundo = 0
        x_fundo -= velocidade
        
        jogador.pontos += 1
        if jogador.pontos % 100 == 0:
            velocidade +=1

        texto = font.render("Pontuação: " + str(jogador.pontos) , True, (0,0,0))
        xy_texto = texto.get_rect()
        xy_texto.center = (900,50)
        window.blit(texto, xy_texto)

        all_sprites.update(velocidade)
        all_sprites.draw(window)
        window.blit(jogador.image,(35,jogador.rect.y))

        pygame.display.update()
    print('saiu jogo')
    return estado, jogador.pontos

def inicio():
    estado = 0
    while estado == 0:
        window.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        mensagem = font.render("Clique em qualquer tecla para começar", True, (0, 0, 0))
        mensagem_rect = mensagem.get_rect()
        mensagem_rect.center = (WIDTH // 2, HEIGHT // 2)
        window.blit(mensagem, mensagem_rect)
        window.blit(correndo[0], (WIDTH // 2 - 20, HEIGHT // 2 - 140))
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                estado = 2
            if evento.type == pygame.QUIT:
                estado = -1
    print('saiu inicio')
    return estado

def game_over(pontos):

    estado = 9

    while estado == 9:
        window.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                estado = 2
            if evento.type == pygame.QUIT:
                estado = -1

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

    print('saiu game over')
    return estado


estado = 0
pontos = 0
while True:
    print(f'estado: {estado} - pontos: {pontos}')
    if estado == -1: break
    elif estado == 0: estado = inicio()
    elif estado == 2: estado, pontos = jogo()
    elif estado == 9: estado = game_over(pontos)
print('Volte sempre!')
