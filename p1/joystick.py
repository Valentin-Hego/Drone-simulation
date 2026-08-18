import pygame
import sys

pygame.init()
pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()
#print(joystick) print l'@ du joystick

# pygame setup
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True

# Position du rectangle
x = 350
y = 200
tir = pygame.Rect(x, y, 100, 100)
tir_actif = False

SEUIL = 0.1

while running:

    # Gestion des événements
    for event in pygame.event.get():
        #print(event, flush=True)
        if event.type == pygame.QUIT:
            running = False

        # Bouton 0 appuyé
        elif event.type == pygame.JOYBUTTONDOWN and event.button == 0:
            tir_actif = True
            print("TIR", flush=True)


        # Bouton 0 relâché
        elif event.type == pygame.JOYBUTTONUP and event.button == 0:
            tir_actif = False
            print("NEUTRE", flush=True)

    # Lecture des axes
    axe_0 = joystick.get_axis(0)
    axe_1 = joystick.get_axis(1)
    axe_2 = joystick.get_axis(2)
    axe_3 = joystick.get_axis(3)

    '''
    print(f"axe 0 : {axe_0:.2f}")
    print(f"axe 1 : {axe_1:.2f}")
    print(f"axe 2 : {axe_2:.2f}")
    print(f"axe 3 : {axe_3:.2f}")
    print("------------------------------")
    '''

    screen.fill("black")

    ordre_actuel = "NEUTRE"

    if tir_actif:
        ordre_actuel = "TIR"
        tir.topleft = (x, y)
        pygame.draw.rect(screen, "red", tir)

    # Flèche selon la direction du joystick
    else:
        if axe_0 > SEUIL and axe_1 < -SEUIL:      # NORD-EST
            pygame.draw.polygon(screen, "white",
                [(335,165), (270,165), (285,180),
                (240,225), (255,240), (300,195),
                (315,210)])
            ordre_actuel = "NE"

        elif axe_0 > SEUIL and axe_1 > SEUIL:     # SUD-EST
            pygame.draw.polygon(screen, "white",
                [(335,235), (315,190), (300,205),
                (255,160), (240,175), (285,220),
                (270,235)])
            ordre_actuel = "SE"

        elif axe_0 < -SEUIL and axe_1 < -SEUIL:   # NORD-OUEST
            pygame.draw.polygon(screen, "white",
                [(265,165), (330,165), (315,180),
                (360,225), (345,240), (300,195),
                (285,210)])
            ordre_actuel = "NO"

        elif axe_0 < -SEUIL and axe_1 > SEUIL:    # SUD-OUEST
            pygame.draw.polygon(screen, "white",
                [(265,235), (285,190), (300,205),
                (345,160), (360,175), (315,220),
                (330,235)])
            ordre_actuel = "SO"

        elif axe_1 < -SEUIL:                      # NORD
            pygame.draw.polygon(screen, "white",
                [(300,150), (270,200), (290,200),
                (290,240), (310,240), (310,200),
                (330,200)])
            ordre_actuel = "N"

        elif axe_1 > SEUIL:                       # SUD
            pygame.draw.polygon(screen, "white",
                [(300,250), (270,200), (290,200),
                (290,160), (310,160), (310,200),
                (330,200)])
            ordre_actuel = "S"

        elif axe_0 > SEUIL:                       # EST
            pygame.draw.polygon(screen, "white",
                [(350,200), (300,170), (300,190),
                (260,190), (260,210), (300,210),
                (300,230)])
            ordre_actuel = "E"

        elif axe_0 < -SEUIL:                      # OUEST
            pygame.draw.polygon(screen, "white",
                [(250,200), (300,170), (300,190),
                (340,190), (340,210), (300,210),
                (300,230)])
            ordre_actuel = "O"

        elif (axe_0 < SEUIL) and (axe_1 < SEUIL): # remise a 0
            ordre_actuel = "NEUTRE"

    print(ordre_actuel, flush=True)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()