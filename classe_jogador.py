import pygame
from caminho_relativo import resource_path

class Jogador:
    def __init__ (self):
        self.pos_x = 430
        self.pos_y = 861
        self.lista_sprite = [pygame.transform.scale_by(pygame.image.load(resource_path("src/img/sprints-spongeboob.png")),2.5),
                             pygame.transform.scale_by(pygame.image.load(resource_path("")),2.5),
                             pygame.transform.scale_by(pygame.image.load(resource_path("")),2.5),
                            
                             ]
        self.contador = 0
        self.sprite = self.lista_sprite[self.contador]
        self.mascara = pygame.mask.from_surface(self.sprite)
        self.imagem = self.sprite

    def andar (self,tecla_pressionada):
        movendo = tecla_pressionada[pygame.K_RIGHT] or tecla_pressionada[pygame.K_LEFT]
        if movendo:
            self.contador += 1
            if self.contador == len(self.lista_sprite):
                self.contador = 0
            self.sprite = self.lista_sprite[self.contador]
            if tecla_pressionada[pygame.K_RIGHT] or tecla_pressionada[pygame.K_d]:
                if self.pos_x < 900 - self.imagem.get_width():    
                    self.pos_x += 10
                    self.imagem = self.sprite
            if tecla_pressionada[pygame.K_LEFT] or tecla_pressionada[pygame.K_a]:
                if self.pos_x > 0 :
                    self.pos_x -= 10
                    
                    self.imagem = pygame.transform.flip(self.sprite,True,False)
        else:
            self.sprite = self.lista_sprite[0]
    
    def exibir (self,tela_do_jogo):
        tela_do_jogo.blit(self.imagem,(self.pos_x,self.pos_y))

        