import pygame
import os
import random

pygame.init()

#pegando as imagens
correndo = [
    pygame.image.load(os.path.join("Pygame-certo\dinossauro", "DinoRun1.png")),
    pygame.image.load(os.path.join("Pygame-certo\dinossauro", "DinoRun2.png"))
]
pulando = [
    pygame.image.load(os.path.join("Pygame-certo\dinossauro", "DinoJump.png"))
]
mergulho = [
    pygame.image.load(os.path.join("Pygame-certo\dinossauro", "DinoDuck1.png")),
    pygame.image.load(os.path.join("Pygame-certo\dinossauro", "DinoDuck2.png"))
]
cactusP = [
    pygame.image.load(os.path.join("Pygame-certo\cactus", "SmallCactus1.png")),
    pygame.image.load(os.path.join("Pygame-certo\cactus", "SmallCactus2.png")), 
    pygame.image.load(os.path.join("Pygame-certo\cactus", "SmallCactus3.png"))
]
cactusG = [
    pygame.image.load(os.path.join("Pygame-certo\cactus", "LargeCactus1.png")), 
    pygame.image.load(os.path.join("Pygame-certo\cactus", "LargeCactus2.png")), 
    pygame.image.load(os.path.join("Pygame-certo\cactus", "LargeCactus3.png"))
]
passaro = [
    pygame.image.load(os.path.join("Pygame-certo\passaro", "Bird1.png")), 
    pygame.image.load(os.path.join("Pygame-certo\passaro", "Bird2.png"))
]
nuvens_img = pygame.image.load(os.path.join("Pygame-certo\ceu", "nuvem.png"))
cenario = pygame.image.load(os.path.join("Pygame-certo\chao", "chao.png"))
bullet_img = pygame.image.load(os.path.join("Pygame-certo/bullet\laserRed16_virado.png"))