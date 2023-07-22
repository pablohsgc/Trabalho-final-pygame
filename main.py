from typing import Any
import pygame
import sys

class Personagem(pygame.sprite.Sprite):
    def __init__(self,largura,altura,x,y,velocidade):
        super().__init__()
        self.velocidade = velocidade

        #definicao da aparencia do sprite
        self.image = pygame.Surface([largura,altura])
        self.image.fill((0,0,255)) # se voce possuir uma imagem, essa linha não será necessária

        #posicionando o sprite
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
        
    def update(self):
        pass

    def move_esquerda(self):
        self.rect.x -= self.velocidade

    def move_direita(self):
        self.rect.x += self.velocidade


pygame.init()
clock = pygame.time.Clock()

largura = 600
altura = 600

janela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("SPACE INVADERS - Pablo Henrique")

#grupos de sprites
grupo_mostros = pygame.sprite.Group()
grupo_personagem = pygame.sprite.Group()
grupo_disparos = pygame.sprite.Group()

#adicionar os sprites no grupo
personagem = Personagem(35,35,285,560,5)
grupo_personagem.add(personagem)

#faca aqui a criacao dos sprites dos monstros
# ---
# ---

#faca aqui a adicao dos monstros nos grupos de sprites
# ---
# ---

tecla_esquerda_pressionada = False
tecla_direita_pressionada = False

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                tecla_esquerda_pressionada = True
            elif evento.key == pygame.K_RIGHT:
                tecla_direita_pressionada = True

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT:
                tecla_esquerda_pressionada = False
            elif evento.key == pygame.K_RIGHT:
                tecla_direita_pressionada = False
    
    if tecla_esquerda_pressionada:
        personagem.move_esquerda()
    elif tecla_direita_pressionada: 
        personagem.move_direita()

    janela.fill((0,0,0))

    #atualizacao dos grupos
    grupo_personagem.update()
    grupo_mostros.update()
    grupo_disparos.update()

    #desenhando sprites na tela
    grupo_personagem.draw(janela)
    grupo_mostros.draw(janela)
    grupo_disparos.draw(janela)

    pygame.display.flip()
    clock.tick(60)
