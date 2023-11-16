import pygame
import os
import random
pygame.init()

# Tela
WIDTH = 1000
HEIGHT = 500
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('T-rex running')

parado = pygame.image.load(os.path.join("Pygamecerto\dinossauro", "DinoStart.png"))
correndo = [pygame.image.load(os.path.join("Pygamecerto\dinossauro", "DinoRun1.png")), pygame.image.load(os.path.join("Pygamecerto\dinossauro", "DinoRun2.png"))]
pulando = pygame.image.load(os.path.join("Pygamecerto\dinossauro", "DinoJump.png"))
dinobaixo = [pygame.image.load(os.path.join("Pygamecerto\dinossauro", "DinoDuck1.png")), pygame.image.load(os.path.join("Pygamecerto\dinossauro", "DinoDuck2.png"))]

cactusP = [pygame.image.load(os.path.join("Pygamecerto\cactus", "SmallCactus1.png")), pygame.image.load(os.path.join("Pygamecerto\cactus", "SmallCactus2.png")), pygame.image.load(os.path.join("Pygamecerto\cactus", "SmallCactus3.png"))]
cactusG = [pygame.image.load(os.path.join("Pygamecerto\cactus", "LargeCactus1.png")), pygame.image.load(os.path.join("Pygamecerto\cactus", "LargeCactus2.png")), pygame.image.load(os.path.join("Pygamecerto\cactus", "LargeCactus3.png"))]

passaro = [pygame.image.load(os.path.join("Pygamecerto\passaro", "Bird1.png")), pygame.image.load(os.path.join("Pygamecerto\passaro", "Bird2.png"))]

nuvens = pygame.image.load(os.path.join("Pygamecerto\ceu", "nuvem.png"))

cenario = pygame.image.load(os.path.join("Pygamecerto\chao", "chao.png"))


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