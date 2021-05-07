# ==================================
# Per prima cosa importiamo le librerie
# che ci serviranno successivamente
# ==================================
import pygame, random
pygame.init()

# ==================================
# Facciamo si che il programma possa prendere
# le immagine dalle cartelle e le inseriamo in delle variabili
# ==================================
MASCHERINA = pygame.image.load('immagini\IMMAIGNI DEL COVID/mascherina immagine disegno.png')
sfondo = pygame.image.load('immagini\IMMAIGNI DEL COVID/sfondo.png')
gameover=pygame.image.load('immagini\immagini\gameover.png')
molecola_covid = pygame.image.load('immagini/IMMAIGNI DEL COVID/molecola covid.png')
SCHERMO = pygame.display.set_mode((1024,1024))
font = pygame.font.SysFont('Comics Sans MS',50,bold=True)
# ==================================
# inizializziamo le prime variabili
# ==================================
avanzamento,fps, punti = 15, 50, 0

# ==================================
# Creiamo una classe che ci serivrà
# successivamente per creare e far
# muovere la "molecola"
# ==================================

class virus_classe:
    # =================================
    # impostiamo con random la posizione sull'asse X di ogni elemento
    # della classe cosi da renderlo imprevedibile entro un certo range
    # =================================
    def __init__(self): self.x , self.y , self.preso  = random.randint(50,950),-50 , False

    def avanza_e_disegna(self):
        # =================================
        # impostiamo l'operazione che farà si che la molecola
        # scenda più o meno velocemente
        # =================================
        self.y += avanzamento
        SCHERMO.blit(molecola_covid,(self.x,self.y))

    def collisione(self,bas):
        # =================================
        # Inizializziamo altre variabili che saranno utili all'interno
        # della classe
        # =================================
        mascherina_lato_dx , mascherina_lato_sx,virus_lato_dx , virus_lato_sx , mascherina_lato_su , mascherina_lato_giu,virus_lato_giu = bas+ MASCHERINA.get_width()-80, bas,self.x + molecola_covid.get_width()-80 , self.x, 525 , 525 + MASCHERINA.get_width() - 30,self.y
        global punti
        # =================================
        # Creaiamo le condizioni di "Contatto fra
        # un elemento e l'altro e il successivo aumento di punti
        # =================================
        if (mascherina_lato_su < virus_lato_giu and mascherina_lato_sx < virus_lato_dx and virus_lato_dx < mascherina_lato_dx and mascherina_lato_giu > virus_lato_giu) or (mascherina_lato_su < virus_lato_giu and mascherina_lato_dx > virus_lato_sx and mascherina_lato_sx < virus_lato_sx and mascherina_lato_giu > virus_lato_giu):
            punti,self.y,self.preso = punti + 1,self.y + 500,True

        # =================================
        # Scriviamo la condizione di "Sconfitta"
        # quando l' elemento scende troppo
        # =================================
        elif mascherina_lato_giu < virus_lato_giu and self.preso == False:
            SCHERMO.blit(gameover, (425, 450))
            SCHERMO.blit(punti_render,(512,40))
            aggiorna()
            while True:
                # =================================
                # creiamo un ciclo che blocchi il gioco
                # =================================
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: pygame.quit()

    #=================================
    #Costruiamo una funzione che disegni gli oggetti
    #=================================
def disegna_oggetti():
    SCHERMO.blit(sfondo,(0,0))
    for t in virus:
        t.avanza_e_disegna()
        t.collisione(bas)
    SCHERMO.blit(MASCHERINA,(bas ,650))
    global punti_render
    punti_render = font.render(str(punti), 50, (255, 255, 255))
    SCHERMO.blit(punti_render,(512,40))

    # =================================
    # Successivamente ne creaimo un altra che li faccia mostrare
    # aggiornando ogni volta la pagina
    # =================================
def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(fps)


#=================================
#inizializziamo altre variabili
#=================================
punti, bas,virus =0 , 350,[]
virus.append(virus_classe())

#=================================
#Scriviamo il ciclo principale dal quale verranno
# richiamate tutte le funzioni
#=================================
while True:
    aggiorna()
    disegna_oggetti()
    # =================================
    # controlliamo l'input da tastiera
    # =================================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:pygame.quit()
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):bas = bas +50
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):bas = bas - 50
    # =================================
    #Creiamo una nuova entità ogni qual volta
    #una scenda troppo dopo essere stata presa
    # =================================
    if virus[-1].y> 400:virus.append(virus_classe())
