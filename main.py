import pygame
from caminho_relativo import resource_path
from classe_jogador import Jogador
from classe_ruim import Ruim

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
            Ruim(resource_path("src/img/fanstasma_normal.png")),
            Ruim(resource_path("src/img/fanstasma_forte.png")),
            Ruim(resource_path("src/img/balde_lixo.png")),
            Ruim(resource_path("src/img/plancton.png"))
            ]

x = 900
y = 1000
clock = pygame.time.Clock()
#cria a janela do jogo
tela = pygame.display.set_mode((x,y))
fundo = pygame.image.load(resource_path("src/img/fundo.png"))
fundo = pygame.transform.scale(fundo,(x,y))

rodando = True
pontos = 0
vidas = 5

sponge_bob = Jogador()
fonte_texto = pygame.font.SysFont("Arial",28,True)
status_jogo = "PLAY"

while rodando :
    lista_de_eventos = pygame.event.get()
    for evento in lista_de_eventos:
        if evento.type == pygame.QUIT:
            rodando = False
    
    tecla_pressionada = pygame.key.get_pressed()

   # if status_jogo == "INICIO":
       # if tecla_pressionada[pygame.K_RETURN]:
          #  status_jogo = "PLAY"
        #montar tela inicial depois

    if status_jogo == "PLAY":
        tela.blit(fundo,(0,0))

        sponge_bob.exibir(tela)
        sponge_bob.andar(tecla_pressionada)
        for inimigo in inimigos:
            inimigo.exibir(tela)
            inimigo.andar()

            if inimigo.mascara.overlap(sponge_bob.mascara,(sponge_bob.pos_x - inimigo.pos_x , sponge_bob.pos_y - inimigo.pos_y )):
                print("bateu")
                inimigo.voltar()
                vidas -= 1
            if vidas == 0:
                status_jogo = "PERDEU"
            

    pygame.display.update()

    clock.tick(60)
