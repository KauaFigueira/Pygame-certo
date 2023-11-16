import pygame
import os
import random
pygame.init()

# Tela
WIDTH = 1000
HEIGHT = 500
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('T-rex running')

parado = pygame.image.load(os.path.join("dinossauro", "DinoStart.png"))
correndo = [pygame.image.load(os.path.join("dinossauro", "DinoRun1.png")), pygame.image.load(os.path.join("dinossauro", "DinoRun2.png"))]
pulando = pygame.image.load(os.path.join("dinossauro", "DinoJump.png"))
dinobaixo = [pygame.image.load(os.path.join("dinossauro", "DinoDuck1.png")), pygame.image.load(os.path.join("dinossauro", "DinoDuck2.png"))]

cactusP = [pygame.image.load(os.path.join("Cactus", "SmallCactus1.png")), pygame.image.load(os.path.join("Cactus", "SmallCactus2.png")), pygame.image.load(os.path.join("Cactus", "SmallCactus3.png"))]
cactusG = [pygame.image.load(os.path.join("Cactus", "LargeCactus1.png")), pygame.image.load(os.path.join("Cactus", "LargeCactus2.png")), pygame.image.load(os.path.join("Cactus", "LargeCactus3.png"))]

passaro = [pygame.image.load(os.path.join("passaro", "Bird1.png")), pygame.image.load(os.path.join("passaro", "Bird2.png"))]

nuvens = pygame.image.load(os.path.join("nuvem", "nuvem.png"))

cenario = pygame.image.load(os.path.join("chao", "chao.png"))


game = True
clock = pygame.time.Clock()

while game:
    
    clock.tick(30)
    # Trata eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False



    # ----- Gera saídas
    window.fill((255, 255, 255))  

    pygame.display.update()