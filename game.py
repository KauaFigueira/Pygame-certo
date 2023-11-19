import pygame
import os
import random

pygame.init()

# Tela
WIDTH = 1000
HEIGHT = 500
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('T-rex running')

#pegando as imagens
correndo = [
    pygame.image.load(os.path.join("Pygame-certo\dinossauro", "DinoRun1.png")),
    pygame.image.load(os.path.join("Pygame-certo\dinossauro", "DinoRun2.png"))
]
pulando = pygame.image.load(os.path.join("Pygame-certo\dinossauro", "DinoJump.png"))
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
nuvens = pygame.image.load(os.path.join("Pygame-certo\ceu", "nuvem.png"))
cenario = pygame.image.load(os.path.join("Pygame-certo\chao", "chao.png"))

# Criando uma classe para o dinossauro/jogador
class Dinossauro:
    x = 35
    y = 280
    #para ele se abaixar precisa de um Y menor do que ele correndo (nesse caso maior pq plano invertido)
    y_mergulho = 340
    VEL_PULO= 8.5

    def __init__(self):
        self.abaixado_img = mergulho
        self.correndo_img = correndo
        self.pulando_img = pulando

        #determinando estado basico do personagem
        self.abaixado = False
        self.pulando = False
        self.correndo = True

        self.passos = 0
        self.vel_pulo = self.VEL_PULO
        self.image = self.correndo_img[self.passos]
        self.dinossauro_rect = self.image.get_rect()
        self.dinossauro_rect.x = self.x
        self.dinossauro_rect.y = self.y

    def update(self, entrada):
        if self.correndo:
            self.correr()
        if self.abaixado:
            self.mergulho()
        if self.pulando:
            self.pular()

        #Se ele nao fizer nada, continuar correndo
        if not entrada[pygame.K_UP] and not entrada[pygame.K_DOWN]:
            self.abaixado = False
            self.pulando = False
            self.correndo = True
        #Se ele estiver pulando ele nao pode mergulhar
        elif entrada[pygame.K_DOWN] and not self.pulando:
            self.abaixado = True
            self.pulando = False
            self.correndo = False
        #Se ele ja estiver pulando ou pulado nao queremos que ele pule de novo
        elif entrada[pygame.K_UP] and not self.pulando:
            self.pulando = True
            self.abaixado = False
            self.correndo = False
    #como ele mergulha(Abaixa)
    def mergulho(self):
        if self.passos >= 8:
            self.passos = 0

        self.image = self.abaixado_img[self.passos // 4]
        self.dinossauro_rect = self.image.get_rect()
        self.dinossauro_rect.x = self.x
        self.dinossauro_rect.y = self.y_mergulho
        self.passos += 1
    #como ele corre 
    def correr(self):
        if self.passos >= 8:
            self.passos = 0

        self.image = self.correndo_img[self.passos // 4]
        self.dinossauro_rect = self.image.get_rect()
        self.dinossauro_rect.x = self.x
        self.dinossauro_rect.y = self.y
        self.passos += 1
    #Como ele pula
    def pular(self):
        self.image = self.pulando_img
        if self.pulando:
            self.dinossauro_rect.y -= self.vel_pulo * 4
            self.vel_pulo -= 0.8
        if self.vel_pulo < - self.VEL_PULO:
            self.pulando = False
            self.vel_pulo = self.VEL_PULO

    def desenho(self, window):
        window.blit(self.image, (self.dinossauro_rect.x, self.dinossauro_rect.y))

class nuvem:
    def __init__(self):
        self.x = WIDTH + random.randint(800,1000)
        self.y = random.randint(50,100)
        self.image = nuvens
        self.width = self.image.get_width()

    def update(self):
        self.x = -jogo_velo
        if self.x < -self.width:
            self.x = WIDTH + random.randint(2500,3000)
            self.y = random.randint(50,100)

    def draw(self, screen):
        window.blit(self.image, (self.x,self.y))

def main():
    global jogo_velo
    game = True
    clock = pygame.time.Clock()
    jogador = Dinossauro()
    nuvens = nuvem()
    jogo_velo = 14
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

    jogador.desenho(window)
    jogador.update(entrada)

    nuvens.desenho(window)
    nuvens.update()

    pygame.display.update()
    