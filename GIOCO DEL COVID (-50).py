import pygame, random
pygame.init()
MASCHERINA = pygame.image.load('immagini\IMMAIGNI DEL COVID/mascherina immagine disegno.png')
sfondo = pygame.image.load('immagini\IMMAIGNI DEL COVID/sfondo.png')
gameover=pygame.image.load('immagini\immagini\gameover.png')
molecola_covid = pygame.image.load('immagini/IMMAIGNI DEL COVID/molecola covid.png')
SCHERMO = pygame.display.set_mode((1024,1024))
font = pygame.font.SysFont('Comics Sans MS',50,bold=True)
avanzamento,fps, punti = 15, 50, 0
class virus_classe:
    def __init__(self): self.x , self.y , self.preso  = random.randint(50,950),-50 , False
    def avanza_e_disegna(self):
        self.y += avanzamento
        SCHERMO.blit(molecola_covid,(self.x,self.y))
    def collisione(self,bas):
        mascherina_lato_dx , mascherina_lato_sx,virus_lato_dx , virus_lato_sx , mascherina_lato_su , mascherina_lato_giu,virus_lato_giu = bas+ MASCHERINA.get_width()-80, bas,self.x + molecola_covid.get_width()-80 , self.x, 525 , 525 + MASCHERINA.get_width() - 30,self.y
        global punti
        if (mascherina_lato_su < virus_lato_giu and mascherina_lato_sx < virus_lato_dx and virus_lato_dx < mascherina_lato_dx and mascherina_lato_giu > virus_lato_giu) or (mascherina_lato_su < virus_lato_giu and mascherina_lato_dx > virus_lato_sx and mascherina_lato_sx < virus_lato_sx and mascherina_lato_giu > virus_lato_giu):
            punti,self.y,self.preso = punti + 1,self.y + 500,True
        elif mascherina_lato_giu < virus_lato_giu and self.preso == False:
            SCHERMO.blit(gameover, (425, 450))
            SCHERMO.blit(punti_render,(512,40))
            aggiorna()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: pygame.quit()
def disegna_oggetti():
    SCHERMO.blit(sfondo,(0,0))
    for t in virus:
        t.avanza_e_disegna()
        t.collisione(bas)
    SCHERMO.blit(MASCHERINA,(bas ,650))
    global punti_render
    punti_render = font.render(str(punti), 50, (255, 255, 255))
    SCHERMO.blit(punti_render,(512,40))
def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(fps)

punti, bas,virus =0 , 350,[]
virus.append(virus_classe())

while True:
    aggiorna()
    disegna_oggetti()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:pygame.quit()
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):bas = bas +50
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):bas = bas - 50
    if virus[-1].y> 400:virus.append(virus_classe())