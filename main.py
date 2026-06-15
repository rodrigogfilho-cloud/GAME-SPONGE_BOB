import pygame
from caminho_relativo import resource_path
from classe_jogador import Jogador
from classe_ruim import Ruim
from classe_bom import Bom
import time

pygame.init()

pygame.display.set_caption("PEGUE O HAMBÚRGUER DE SIRI 🍔🧽")

#LISTAS#

cores = {
    "VERMELHO" : (255,0,0),
    "VERDE DE PASTO" : (70,255,70),
    "PRETO"  : (0,0,0),
    "BRANCO" : (255,255,255)
}

inimigos = [Ruim(resource_path("src/img/fanstasma_normal.png")),
            Ruim(resource_path("src/img/fanstasma_forte.png")),
            Ruim(resource_path("src/img/balde_lixo.png")),
            Ruim(resource_path("src/img/plancton.png")),
            ]

bens = [Bom(resource_path("src/img/agua_viva.png")),
        Bom(resource_path("src/img/sr-sirigueijo.png")),
        Bom(resource_path("src/img/patrick.png")),
        Bom(resource_path("src/img/garry.png")),
        ]



x = 900
y = 1000
clock = pygame.time.Clock()
#cria a janela do jogo
tela = pygame.display.set_mode((x,y))
fundo = pygame.image.load(resource_path("src/img/fundo.png"))
fundo = pygame.transform.scale(fundo,(x,y))
inicio = pygame.image.load(resource_path("src/img/tela-inicio.png"))
inicio = pygame.transform.scale(inicio,(x,y))
derrota = pygame.image.load(resource_path("src/img/derrota.png"))
derrota = pygame.transform.scale(derrota,(x,y))
vitoria = pygame.image.load(resource_path("src/img/vitoria.png"))
vitoria = pygame.transform.scale(vitoria,(x,y))
rodando = True
pontos = 0
vidas = 5

sponge_bob = Jogador()
fonte_texto = pygame.font.SysFont("Arial",28,True)
contador_poder = 3
status_jogo = "INICIO"



while rodando :
    lista_de_eventos = pygame.event.get()
    for evento in lista_de_eventos:
        if evento.type == pygame.QUIT:
            rodando = False
    
    tecla_pressionada = pygame.key.get_pressed()

    if status_jogo == "INICIO":
        tela.blit(inicio,(0,0))
        if tecla_pressionada[pygame.K_RETURN] or tecla_pressionada[pygame.K_KP_ENTER]:
            status_jogo = "PLAY"

    if status_jogo == "PLAY":

        
        tela.blit(fundo,(0,0))

        #PONTUAÇÃO JOGO
        textos_pontos = fonte_texto.render(f' PONTOS: {pontos} ', False,(255,255,255),(0,0,0))
        tela.blit(textos_pontos,(15, 20))
        textos_mortes = fonte_texto.render(f' VIDAS: {vidas} ', False,(255,255,255),(0,0,0))
        tela.blit(textos_mortes,(775, 20))
        textos_limite = fonte_texto.render(f' CRÉDITOS DE PODER : {contador_poder} ', False,(255,255,255),(0,0,0))
        tela.blit(textos_limite,(310,20))

        #BOB ESPONJA ANDANDO

        sponge_bob.exibir(tela)
        sponge_bob.andar(tecla_pressionada)

        for inimigo in inimigos:
            inimigo.exibir(tela)
            inimigo.andar()

            if inimigo.mascara.overlap(sponge_bob.mascara,(sponge_bob.pos_x - inimigo.pos_x , sponge_bob.pos_y - inimigo.pos_y )):
                inimigo.voltar()
                vidas -= 1

        for amigo in bens:
            amigo.exibir(tela)
            amigo.andar()

            if amigo.mascara.overlap(sponge_bob.mascara,(sponge_bob.pos_x - amigo.x , sponge_bob.pos_y - amigo.y )):
                amigo.voltar()
                pontos += 1

        if tecla_pressionada[pygame.K_SPACE]:
            contador_poder -= 1
            for inimigo in inimigos:
                inimigo.pos_y = -2500
            
            

        if contador_poder == 0:
            print("SEU PODER NAO FUNCIONA")

                

        if vidas == 0:
            status_jogo = "PERDEU"

        if pontos == 20 : 
            status_jogo = "GANHOU"
    
    if status_jogo == "PERDEU":

        tela.blit(derrota,(0,0))
        if tecla_pressionada[pygame.K_SPACE]:

            for inimigo in inimigos:
                inimigo.voltar()
            for amigo in bens :
                amigo.voltar()

            vidas = 5
            pontos = 0 
            status_jogo = "PLAY"

    if status_jogo == "GANHOU":

        tela.blit(vitoria,(0,0))
        if tecla_pressionada[pygame.K_RETURN] or tecla_pressionada[pygame.K_KP_ENTER]:

            for inimigo in inimigos:
                inimigo.voltar()
            for amigo in bens :
                amigo.voltar()

            vidas = 5
            pontos = 0 
            status_jogo = "PLAY"
    if tecla_pressionada[pygame.K_ESCAPE]:
        rodando = False

    pygame.display.update()

    clock.tick(30)
