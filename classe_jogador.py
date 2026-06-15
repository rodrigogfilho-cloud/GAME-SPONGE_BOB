import pygame
from caminho_relativo import resource_path

class Jogador:
    def __init__ (self):
        self.pos_x = 430
        self.pos_y = 862
        self.parado = pygame.transform.scale_by(pygame.image.load(resource_path("src/img/sprints-spongeboob.png")),2.5)
        self.lista_sprite = [
                             pygame.transform.scale_by(pygame.image.load(resource_path("src/img/sprite1.png")),2.5),
                             pygame.transform.scale_by(pygame.image.load(resource_path("src/img/sprite2.png")),2.5),
                             pygame.transform.scale_by(pygame.image.load(resource_path("src/img/sprite3.png")),2.5),
                             pygame.transform.scale_by(pygame.image.load(resource_path("src/img/sprite4.png")),2.5),
                             pygame.transform.scale_by(pygame.image.load(resource_path("src/img/sprite5.png")),2.4),
                             pygame.transform.scale_by(pygame.image.load(resource_path("src/img/sprite6.png")),2.4),
                             pygame.transform.scale_by(pygame.image.load(resource_path("src/img/sprite7.png")),2.4),
                             pygame.transform.scale_by(pygame.image.load(resource_path("src/img/sprite8.png")),2.5),
                             pygame.transform.scale_by(pygame.image.load(resource_path("src/img/sprite9.png")),2.4)
                            
                             ]
        self.contador = 0
        self.sprite = self.lista_sprite[self.contador]
        self.mascara = pygame.mask.from_surface(self.sprite)
        self.imagem = self.sprite

    def andar (self,tecla_pressionada):
        movendo = tecla_pressionada[pygame.K_RIGHT] or tecla_pressionada[pygame.K_LEFT] or tecla_pressionada[pygame.K_d] or tecla_pressionada[pygame.K_a]
        if movendo:
            self.contador += 1
            if self.contador == len(self.lista_sprite):
                self.contador = 0
            self.sprite = self.lista_sprite[self.contador]
            if tecla_pressionada[pygame.K_RIGHT] or tecla_pressionada[pygame.K_d]:
                if self.pos_x < 900 - self.imagem.get_width():    
                    self.pos_x += 5.5
                    self.imagem = self.sprite
            if tecla_pressionada[pygame.K_LEFT] or tecla_pressionada[pygame.K_a]:
                if self.pos_x > 0 :
                    self.pos_x -= 5.5
                    
                    self.imagem = pygame.transform.flip(self.sprite,True,False)
            if tecla_pressionada[pygame.K_LEFT] and tecla_pressionada[pygame.K_RIGHT] or tecla_pressionada[pygame.K_a] and tecla_pressionada[pygame.K_d] or tecla_pressionada[pygame.K_LEFT] and tecla_pressionada[pygame.K_d] or tecla_pressionada[pygame.K_a] and tecla_pressionada[pygame.K_RIGHT]:
                self.imagem = self.parado
            

        else:
            self.imagem = self.parado
            
        
    
    def exibir (self,tela_do_jogo):
        tela_do_jogo.blit(self.imagem,(self.pos_x,self.pos_y))

        