import pygame
import random

class Ruim:

    def __init__(self, endereco_imagem):
        self.imagem =  pygame.image.load(endereco_imagem)
        self.imagem = pygame.transform.scale_by (self.imagem,1)

        self.pos_x = random.randint(100,600)

        self.pos_y = -200
        self.mascara =pygame.mask.from_surface(self.imagem)

        self.velocidade = random.randint(3,5)
    
    def andar (self):
        self.pos_y = self.pos_y + self.velocidade
        if self.pos_y > 1000 :
            self.voltar()

    def exibir (self, tela_jogo):
        tela_jogo.blit(self.imagem,(self.pos_x,self.pos_y)) 

    def voltar (self):
        self.pos_y = -200
        self.pos_x = random.randint(100,600)
        
    


