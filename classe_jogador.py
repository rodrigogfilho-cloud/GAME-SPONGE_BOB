import pygame
from caminho_relativo import resource_path

class Jogador:
    def __init__ (self):
        self.pos_x = 400
        self.pos_y = 850
        self.parado = pygame.transform.scale_by(pygame.image.load(resource_path("src/img/parado.png")),0.8)
        self.lista_sprite = [
                             pygame.transform.scale_by(pygame.image.load(resource_path("src/img/1.png")),1),
                             pygame.transform.scale_by(pygame.image.load(resource_path("src/img/2.png")),1),
                             pygame.transform.scale_by(pygame.image.load(resource_path("src/img/3.png")),1),
                             pygame.transform.scale_by(pygame.image.load(resource_path("src/img/4.png")),1),
                             pygame.transform.scale_by(pygame.image.load(resource_path("src/img/5.png")),1),
                             pygame.transform.scale_by(pygame.image.load(resource_path("src/img/6.png")),1),
                             pygame.transform.scale_by(pygame.image.load(resource_path("src/img/7.png")),1),
                             pygame.transform.scale_by(pygame.image.load(resource_path("src/img/8.png")),1),
                             pygame.transform.scale_by(pygame.image.load(resource_path("src/img/9.png")),1),
                             pygame.transform.scale_by(pygame.image.load(resource_path("src/img/10.png")),1),
                             pygame.transform.scale_by(pygame.image.load(resource_path("src/img/11.png")),1)
                            
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
                    self.pos_x += 5
                    self.imagem = self.sprite

            if tecla_pressionada[pygame.K_LEFT] or tecla_pressionada[pygame.K_a]:
                if self.pos_x > 0 :
                    self.pos_x -= 5
                    self.imagem = pygame.transform.flip(self.sprite,True,False)

            if tecla_pressionada[pygame.K_LEFT] and tecla_pressionada[pygame.K_RIGHT] or tecla_pressionada[pygame.K_a] and tecla_pressionada[pygame.K_d] or tecla_pressionada[pygame.K_LEFT] and tecla_pressionada[pygame.K_d] or tecla_pressionada[pygame.K_a] and tecla_pressionada[pygame.K_RIGHT]:
                self.imagem = self.parado
            

        else:
            self.imagem = self.parado
            
        
    
    def exibir (self,tela_do_jogo):
        tela_do_jogo.blit(self.imagem,(self.pos_x,self.pos_y))

        