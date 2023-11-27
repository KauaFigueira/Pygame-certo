import pygame
import os
import random

pygame.init()

#pegando as imagens
correndo = [
    pygame.image.load(os.path.join("dinossauro", "DinoRun1.png")),
    pygame.image.load(os.path.join("dinossauro", "DinoRun2.png"))
]
pulando = [
    pygame.image.load(os.path.join("dinossauro", "DinoJump.png"))
]
mergulho = [
    pygame.image.load(os.path.join("dinossauro", "DinoDuck1.png")),
    pygame.image.load(os.path.join("dinossauro", "DinoDuck2.png"))
]
cactusP = [
    pygame.image.load(os.path.join("cactus", "SmallCactus1.png")),
    pygame.image.load(os.path.join("cactus", "SmallCactus2.png")), 
    pygame.image.load(os.path.join("cactus", "SmallCactus3.png"))
]
cactusG = [
    pygame.image.load(os.path.join("cactus", "LargeCactus1.png")), 
    pygame.image.load(os.path.join("cactus", "LargeCactus2.png")), 
    pygame.image.load(os.path.join("cactus", "LargeCactus3.png"))
]
passaro = [
    pygame.image.load(os.path.join("passaro", "Bird1.png")), 
    pygame.image.load(os.path.join("passaro", "Bird2.png"))
]
nuvens_img = pygame.image.load(os.path.join("ceu", "nuvem.png"))
cenario = pygame.image.load(os.path.join("chao", "chao.png"))
bullet_img = pygame.image.load(os.path.join("bullet\laserRed16_virado.png"))