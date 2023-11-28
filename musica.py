import pygame
import os

pygame.init()

pygame.mixer.init()

tiro = pygame.mixer.Sound(os.path.join("Pygamecerto\musica", "pew.wav"))
morte = pygame.mixer.Sound(os.path.join("Pygamecerto\musica", "Minecraft-death-sound.wav"))
run = pygame.mixer.Sound(os.path.join("Pygamecerto\musica", "Super-Mario.wav"))