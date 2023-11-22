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
nuvens_img = pygame.image.load(os.path.join("Pygame-certo\ceu", "nuvem.png"))
cenario = pygame.image.load(os.path.join("Pygame-certo\chao", "chao.png"))

# Criando uma classe para o dinossauro/jogador
class Dinossauro:
    x = 35
    y = 300
    #para ele se abaixar precisa de um Y menor do que ele correndo (nesse caso maior pq plano invertido)
    y_mergulho = 340
    VEL_PULO= 8

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
        self.image = self.pulando_img
        if self.pulando:
            self.dinossauro_rect.y -= self.vel_pulo * 4
            self.vel_pulo -= 0.8
        if self.vel_pulo < - self.VEL_PULO:
            self.pulando = False
            self.vel_pulo = self.VEL_PULO
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

    def desenho(self, window):
        window.blit(self.image, (self.dinossauro_rect.x, self.dinossauro_rect.y))

class Nuvem(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.x = WIDTH + random.randint(800,1000)
        self.rect.y = random.randint(50,100)
        self.image = nuvens_img
        self.width = self.image.get_width()

    def update(self):
        self.rect.x += -jogo_velo
        if self.rect.x < -self.width:
            self.rect.x = WIDTH + random.randint(2500,3000)
            self.rect.y = random.randint(50,100)

    def desenho(self, window):
        window.blit(self.image, (self.x,self.y))

global jogo_velo , x_fundo , y_fundo , pontos
game = True
clock = pygame.time.Clock()
jogador = Dinossauro()
jogo_velo = 14
x_fundo = 0
y_fundo = 380
pontos = 0
font = pygame.font.Font('freesansbold.ttf', 20)

all_sprites = pygame.sprite.Group()
for i in range(4):
    nuvem = Nuvem(nuvens_img)
    all_sprites.add(nuvem)
     

def ponto():
    global pontos , jogo_velo
    pontos += 1
    if pontos % 100 == 0:
        jogo_velo +=1

    texto = font.render("Pontuação: " + str(pontos) , True, (0,0,0))
    xy_texto = texto.get_rect()
    xy_texto.center = (900,50)
    window.blit(texto, xy_texto)

def fundo_tela():
    global x_fundo , y_fundo
    WIDTH_F = cenario.get_width()
    window.blit(cenario , (x_fundo , y_fundo))
    window.blit(cenario , (WIDTH_F + x_fundo , y_fundo))
    if x_fundo <= -WIDTH_F:
        window.blit(cenario , (WIDTH_F + x_fundo , y_fundo))
        x_fundo = 0
    x_fundo -= jogo_velo

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

    all_sprites.update()
    all_sprites.draw(window)
    


    fundo_tela()
    
    ponto()

    pygame.display.update()
    