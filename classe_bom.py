import pygame
import random

class Bom:

    def __init__(self, endereco_imagem):
        self.imagem =  pygame.image.load(endereco_imagem)
        self.imagem = pygame.transform.scale_by (self.imagem,1)

        self.x = random.randint(100,600)

        self.y = -200
        self.mascara =pygame.mask.from_surface(self.imagem)

        self.velocidade = random.randint(3,5)
    
    def andar (self):
        self.y = self.y + self.velocidade
        if self.y > 1000 :
            self.voltar()

    def exibir (self, tela_jogo):
        tela_jogo.blit(self.imagem,(self.x,self.y)) 

    def voltar (self):
        self.y = -200
        self.x = random.randint(100,600)
