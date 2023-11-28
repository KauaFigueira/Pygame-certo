import pygame
import os
import random
from imagens import *
from config import *
from musica import *

pygame.init()

game = True
velocidade = 14
x_fundo = 0
y_fundo = 380
pontos = 0
font = pygame.font.Font('freesansbold.ttf', 20)
mortes = 0

class Dinossauro(pygame.sprite.Sprite):
    x = 35
    y = 300
    #para ele se abaixar precisa de um Y menor do que ele correndo (nesse caso maior pq plano invertido)
    y_mergulho = 340
    
    VEL_PULO = 8

    def __init__(self, imgs, all_sprites, all_bullets, bullet_img):
        pygame.sprite.Sprite.__init__(self)

        self.abaixado_img = imgs[0]
        self.correndo_img = imgs[1]
        self.pulando_img = imgs[2]

        #determinando estado basico do personagem
        self.abaixado = False
        self.pulando = False
        self.correndo = True

        self.passos = 0
        self.vel_pulo = self.VEL_PULO
        self.image = self.correndo_img[0]
        #self.rect = self.image.get_rect()
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
        self.y_mergulho = 340
        self.rect.x = self.x
        self.rect.y = self.y

        self.mask = pygame.mask.from_surface(self.image)
        self.all_sprites = all_sprites
        self.all_bullets = all_bullets
        self.bullet_img = bullet_img

        self.pontos = 0
        self.municao = -1

    def update(self, entrada):
        if self.pontos % 1000 == 0:
            self.municao += 1
        if self.correndo:
            self.correr()
        if self.abaixado:
            self.mergulho()
        if self.pulando:
            self.pular()

        
        #Se ele estiver pulando ele nao pode mergulhar
        if entrada[pygame.K_DOWN] and not self.pulando:
            self.abaixado = True
            self.pulando = False
            self.correndo = False
        #Se ele ja estiver pulando ou pulado nao queremos que ele pule de novo
        elif entrada[pygame.K_UP] and not self.pulando:
            self.pulando = True
            self.abaixado = False
            self.correndo = False
        #Se ele nao fizer nada, continuar correndo
        elif not (self.pulando or entrada[pygame.K_DOWN]):
            self.abaixado = False
            self.pulando = False
            self.correndo = True
    #como ele pula
    def pular(self):
        self.image = self.pulando_img[0]
        if self.pulando:
            self.rect.y -= self.vel_pulo * 4
            self.vel_pulo -= 0.8
        if self.vel_pulo < - self.VEL_PULO:
            self.pulando = False
            self.vel_pulo = self.VEL_PULO
    #como ele mergulha(Abaixa)
    def mergulho(self):
        if self.passos >= 8:
            self.passos = 0

        self.image = self.abaixado_img[self.passos // 4]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y_mergulho
        self.passos += 1
    #como ele corre 
    def correr(self):
        if self.passos >= 8:
            self.passos = 0

        self.image = self.correndo_img[self.passos // 4]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.passos += 1

    def shoot(self, entrada):
        if self.municao > 0:
            # A nova bala vai ser criada logo acima e no centro horizontal da nave
            new_bullet = Bullet(self.bullet_img, self.rect.top, self.rect.centerx, entrada)
            self.all_sprites.add(new_bullet)
            self.all_bullets.add(new_bullet)
            self.municao -= 1
            tiro.play()

class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, img, type):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.image = img[self.type]
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.mask = pygame.mask.from_surface(self.image)
    
    def update(self, velocidade):
        self.rect.x -= velocidade
        if -self.rect.width > self.rect.x:
            self.kill()
        

class CactusP(Obstaculo):
    def __init__(self, img):
        super().__init__(img, random.randint(0,2))
        self.rect.y = 320

class CactusG(Obstaculo):
    def __init__(self, img):
        super().__init__(img, random.randint(0,2))
        self.rect.y = 300

class Passaro(Obstaculo):
    def __init__(self,img):
        super().__init__(img, 0)
        self.images = img
        self.rect.y = 270
        self.index = 0
    def update(self, velocidade):
        self.rect.x -= velocidade
        if -self.rect.width > self.rect.x:
            self.kill()
        if self.index >= 8:
            self.index = 0

        x = self.rect.x
        y = self.rect.y
        self.image = self.images[self.index // 4]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.index += 1

class Bullet(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, img, bottom, centerx, entrada):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = centerx
        self.rect.bottom = bottom + 40
        self.speedy = 25  # Velocidade fixa para cima


    def update(self, velocidade):
        # A bala só se move no eixo y
        self.rect.x += self.speedy

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()

class Nuvem(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.x = WIDTH + random.randint(0,200)
        self.rect.y = random.randint(50,100)
        self.image = nuvens_img
        self.width = self.image.get_width()

    def update(self, velocidade):
        self.rect.x += -velocidade
        if self.rect.x < -self.width:
            self.rect.x = WIDTH + random.randint(0,500)
            self.rect.y = random.randint(50,100)

    def desenho(self, window):
        window.blit(self.image, (self.x,self.y))

        

            

                
                    
