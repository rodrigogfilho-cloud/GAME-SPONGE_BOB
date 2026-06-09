import pygame
from caminho_relativo import resource_path

class Jogador:
    def __init__ (self):
        self.pos_x = 430
        self.pos_y = 861
        self.imagem = pygame.image.load(resource_path("src/img/sprints-spongeboob.png"))
        self.imagem = pygame.transform.scale_by(self.imagem,2.5)
        self.mascara = pygame.mask.from_surface(self.imagem)

    def andar (self,tecla_pressionada):

        if tecla_pressionada[pygame.K_RIGHT] or tecla_pressionada[pygame.K_d]:
            if self.pos_x < 900 - self.imagem.get_width():    
                self.pos_x += 10
        if tecla_pressionada[pygame.K_LEFT] or tecla_pressionada[pygame.K_a]:
            if self.pos_x > 0 :
                self.pos_x -= 10
    
    def exibir (self,tela_do_jogo):
        tela_do_jogo.blit(self.imagem,(self.pos_x,self.pos_y))

        