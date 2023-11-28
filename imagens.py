import pygame
import os
import random

pygame.init()

#pegando as imagens
correndo = [
    pygame.image.load(os.path.join("Pygamecerto\dinossauro", "DinoRun1.png")),
    pygame.image.load(os.path.join("Pygamecerto\dinossauro", "DinoRun2.png"))
]
pulando = [
    pygame.image.load(os.path.join("Pygamecerto\dinossauro", "DinoJump.png"))
]
mergulho = [
    pygame.image.load(os.path.join("Pygamecerto\dinossauro", "DinoDuck1.png")),
    pygame.image.load(os.path.join("Pygamecerto\dinossauro", "DinoDuck2.png"))
]
cactusP = [
    pygame.image.load(os.path.join("Pygamecerto\cactus", "SmallCactus1.png")),
    pygame.image.load(os.path.join("Pygamecerto\cactus", "SmallCactus2.png")), 
    pygame.image.load(os.path.join("Pygamecerto\cactus", "SmallCactus3.png"))
]
cactusG = [
    pygame.image.load(os.path.join("Pygamecerto\cactus", "LargeCactus1.png")), 
    pygame.image.load(os.path.join("Pygamecerto\cactus", "LargeCactus2.png")), 
    pygame.image.load(os.path.join("Pygamecerto\cactus", "LargeCactus3.png"))
]
passaro = [
    pygame.image.load(os.path.join("Pygamecerto\passaro", "Bird1.png")), 
    pygame.image.load(os.path.join("Pygamecerto\passaro", "Bird2.png"))
]
nuvens_img = pygame.image.load(os.path.join("Pygamecerto\ceu", "nuvem.png"))
cenario = pygame.image.load(os.path.join("Pygamecerto\chao", "chao.png"))
bullet_img = pygame.image.load(os.path.join("Pygamecerto/bullet\laserRed16_virado.png"))