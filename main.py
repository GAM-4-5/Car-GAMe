import pygame
import random
import time


#ZAPOČINJE PYGAME
pygame.init()

#STVARANJE PROZORA
s_prozor = 1000
v_prozor = 800
prozor = pygame.display.set_mode((s_prozor,v_prozor))
pozadina = pygame.image.load('Untitled (1).png').convert()

#NAZIV PROZORA I LOGO
pygame.display.set_caption("Car GAMe")  #postavlja naslov
logo = pygame.image.load('car.png') #učitava sliku
pygame.display.set_icon(logo)   #postavlja učitanu sliku kao ikonu prozora

#IGRAČ
playerSL = pygame.image.load('player.png')
s_player1 = 100
v_player1 = 64
playerSL = pygame.transform.scale(playerSL, (s_player1, v_player1))
playerX = 500
playerY = 400
playerX_potez = 0
playerY_potez = 0


#OBJEKTI
oilSL = pygame.image.load('oil.png')
s_oil = 60
v_oil = 60
oilSL = pygame.transform.scale(oilSL, (s_oil, v_oil))
oilX = s_prozor
oilY = random.randint(130,(v_prozor - v_oil - 130))   #random koordinate
oilX_potez = 0.3

autoSL = pygame.image.load('player2rot.png')
s_auto = 100
v_auto = 64
autoSL = pygame.transform.scale(autoSL, (s_auto, v_auto))
autoX = s_prozor
autoY = random.randint(130,(v_prozor - v_auto - 130))
autoX_potez = 0.55


def player(x, y):
    prozor.blit(playerSL, (x, y))   #funkcija koja crta sliku igrača u prozoru na mjestu (x, y)
    return

def oil (x, y):
    prozor.blit(oilSL, (x, y))  #funkcija koja crta sliku mrlje ulja na mjestu (x, y)
    return

def auto (x, y):
    prozor.blit(autoSL, (x, y))
    return


#GLAVNA PETLJA
uvjet = True
while uvjet:

    prozor.blit(pozadina, [0, 0])  # postavlja boju ispune prozora

    for event in pygame.event.get():   #provjerava je li stisnut iksić
        if event.type == pygame.QUIT:
            uvjet = False   #ako je iks stisnut mjenja se vrijednost varijable i prozor se zatvara

        #provjerava je li stisnuta tipka gore ili dolje
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:  #ako je stisnuta dolje, pomiče se dolje
                playerY_potez = +0.25
            if event.key == pygame.K_UP: #ako je stisnuta gore, pomiče se gore
                playerY_potez = -0.25
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:   #kada se tipka otpusti, prestaje pomicanje
                playerY_potez = 0

        # provjerava je li stisnuta tipka lijevo ili desno
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # ako je stisnuta lijeva, pmoiče se ulijevo
                playerX_potez = -0.25
            if event.key == pygame.K_RIGHT:  # ako je stisnuta desna, pomiče se udesno
                playerX_potez = 0.25
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:  # kada se tipka otpusti, prestaje pomicanje
                playerX_potez = 0

    playerY += playerY_potez    #izračunava novu Y koordinatu nakon pritiska tipke

    if playerY <= 130:    #određuje granice prozora (visina)
        playerY = 130
    elif playerY > (v_prozor - v_player1 - 130):
        playerY = (v_prozor - v_player1 - 130)

    playerX += playerX_potez    #izračunava novu X koordinatu nakon pritiska tipke

    if playerX <= 0:    #određuje granice prozora (širina)
        playerX = 0
    elif playerX > (s_prozor - s_player1):
        playerX = (s_prozor - s_player1)


    oil(oilX, oilY)     #poziva funkciju oil koja crta sliku mrlje na početnoj poziciji (zatim se koordinate random mjenjaju)
    oilX -= oilX_potez  #promjena koordinate za pomicanje ulijevo
    if oilX < -s_oil:   #provjerava je li slika izašla izvan okvira te ako je stvara novu
        oilX= s_prozor
        oilY = random.randint(130, (v_prozor - v_oil - 130))

    auto(autoX, autoY)
    autoX -= autoX_potez
    if autoX < -s_auto:
        autoX = s_prozor
        autoY = random.randint(130, (v_prozor - v_auto - 130))

    player(playerX, playerY)    #poziva funkciju player koja crta sliku igrača na početnoj poziciji

    pygame.display.update() #vrši update unutar prozora

