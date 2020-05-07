import pygame
import random
import math
import time

# ZAPOČINJE PYGAME
pygame.init()

# STVARANJE PROZORA
s_prozor = 1000
v_prozor = 800
prozor = pygame.display.set_mode((s_prozor, v_prozor))
pozadina = pygame.image.load('Untitled (1).png').convert()

# NAZIV PROZORA I LOGO
pygame.display.set_caption("Car GAMe")  # postavlja naslov
logo = pygame.image.load('car.png')  # učitava sliku
pygame.display.set_icon(logo)  # postavlja učitanu sliku kao ikonu prozora

# SCORE
score = 0
lives = 3
var_1 = False  # varijabla koja provjerava sudar
lives_X = 10
lives_Y = 10
score_X = 180
score_Y = 10
font = pygame.font.Font('freesansbold.ttf', 32)  # font teksta u gornjem lijevom kutu
start = time.time()

# IGRAČ
playerSL = pygame.image.load('player.png')
player_sudar = pygame.image.load('player_sudar.png')
s_player1 = 100
v_player1 = 64
playerSL = pygame.transform.scale(playerSL, (s_player1, v_player1))
player_sudar = pygame.transform.scale(player_sudar, (s_player1, v_player1))
playerX = 500
playerY = 400
playerX_potez = 0
playerY_potez = 0

# OBJEKTI
oilSL = pygame.image.load('oil.png')
s_oil = 60
v_oil = 60
oilSL = pygame.transform.scale(oilSL, (s_oil, v_oil))
oilX = s_prozor
oilY = random.randint(130, (v_prozor - v_oil - 130))  # random koordinate
oilX_potez = 0.3

autoSL = pygame.image.load('player2rot.png')
s_auto = 100
v_auto = 64
autoSL = pygame.transform.scale(autoSL, (s_auto, v_auto))
autoX = s_prozor
autoY = random.randint(130, (v_prozor - v_auto - 130))
autoX_potez = 0.55


def show_text(x1, y1, x2, y2):  # funkcija koja određuje font, lokaciju i boju teksta u gornjem desnom kutu//
    zivoti = font.render("Lives: " + str(lives), True, (0, 0, 0))  # //koji pokazuje broj života i score
    uspjeh = font.render("Score: " + str(score), True, (0, 0, 0))
    prozor.blit(uspjeh, (x2, y2))
    prozor.blit(zivoti, (x1, y1))
    return


def final_score(x=300, y=500):  # funkcija koja određuje font, lokaciju i boju teksta SCORE pri završetku igrice
    final = pygame.font.Font('freesansbold.ttf', 72)
    final_score = final.render("SCORE: " + str(score), True, (245, 0, 0))
    prozor.blit(final_score, (x, y))

    zadnji = pygame.font.Font('freesansbold.ttf', 71)
    zadnji_rez = zadnji.render("SCORE: " + str(score), True, (0, 0, 0))
    prozor.blit(zadnji_rez, (x + 3, y - 0.5))
    return


def game_over(x=100, y=350):  # funkcija koja određuje font, lokaciju i boju teksta GAME OVER
    tekst = pygame.font.Font('freesansbold.ttf', 128)
    game = tekst.render("GAME OVER", True, (245, 0, 0))
    tekst2 = pygame.font.Font('freesansbold.ttf', 127)
    over = tekst2.render("GAME OVER", True, (0, 0, 0))
    prozor.blit(game, (x, y))
    prozor.blit(over, (x + 3, y - 1))
    return


def player(x, y):
    prozor.blit(playerSL, (x, y))  # funkcija koja crta sliku igrača u prozoru na mjestu (x, y)
    return


def oil(x, y):
    prozor.blit(oilSL, (x, y))  # funkcija koja crta sliku mrlje ulja na mjestu (x, y)
    return


def auto(x, y):
    prozor.blit(autoSL, (x, y))  # funkcija koja crta sliku auta iz suprotnog smjera na mjestu (x, y)
    return


def isCollision(playerX, playerY, autoX, autoY, oliX, oilY):  # prati sudar dvaju objekta
    udaljenost_auti = math.sqrt((playerX - autoX) ** 2 + (playerY - autoY) ** 2)  # računa udaljenost auta
    udaljenost_obj = math.sqrt((playerX - oliX) ** 2 + (playerY - oilY) ** 2)  # računa udaljenost objekata
    if udaljenost_auti < 64 or udaljenost_obj < 64:
        return True
    else:
        return False


# GLAVNA PETLJA
uvjet = True
while uvjet:

    prozor.blit(pozadina, [0, 0])  # postavlja boju ispune prozora

    if lives <= 0:
        uvjet = False
        time.sleep(3)

    for event in pygame.event.get():  # provjerava je li stisnut iksić
        if event.type == pygame.QUIT:
            uvjet = False  # ako je iks stisnut mjenja se vrijednost varijable i prozor se zatvara

        # provjerava je li stisnuta tipka gore ili dolje
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:  # ako je stisnuta dolje, pomiče se dolje
                playerY_potez = 0.25
            if event.key == pygame.K_UP:  # ako je stisnuta gore, pomiče se gore
                playerY_potez = -0.25
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:  # kada se tipka otpusti, prestaje pomicanje
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

    playerY += playerY_potez  # izračunava novu Y koordinatu nakon pritiska tipke

    if playerY <= 130:  # određuje granice prozora (visina)
        playerY = 130
    elif playerY > (v_prozor - v_player1 - 130):
        playerY = (v_prozor - v_player1 - 130)

    playerX += playerX_potez # izračunava novu X koordinatu nakon pritiska tipke

    if playerX <= 0:  # određuje granice prozora (širina)
        playerX = 0
    elif playerX > (s_prozor - s_player1):
        playerX = (s_prozor - s_player1)

    oil(oilX,
        oilY)  # poziva funkciju oil koja crta sliku mrlje na početnoj poziciji (zatim se koordinate random mjenjaju)
    oilX -= oilX_potez  # promjena koordinate za pomicanje ulijevo
    if oilX < -s_oil:  # provjerava je li slika izašla izvan okvira te ako je stvara novu
        oilX = s_prozor
        oilY = random.randint(130, (v_prozor - v_oil - 130))
        oilX_potez += (1 / 20)

    auto(autoX, autoY)
    autoX -= autoX_potez
    if autoX < -s_auto:
        autoX = s_prozor
        autoY = random.randint(130, (v_prozor - v_auto - 130))
        autoX_potez += (1 / 20)

    player(playerX, playerY)  # poziva funkciju player koja crta sliku igrača na početnoj poziciji

    # SUDAR
    sudar = isCollision(playerX, playerY, autoX, autoY, oilX, oilY)
    var_2 = sudar
    if sudar:
        prozor.blit(player_sudar, (playerX, playerY))

    if var_1 == False and var_2 == True:  # provjera promjene varijable sudara sa False u True
        lives -= 1

    var_1 = var_2

    if lives == 0:  # ako je broj života jednak nuli, ispisuje GAME OVER i SCORE
        game_over()
        final_score()

    show_text(lives_X, lives_Y, score_X, score_Y)  # ispisuje score i živote u gornjem lijevom kutu

    end = time.time()  # vrijeme trajanja programa
    br = (round(end - start))  # računa score
    score = br

    pygame.display.update()  # vrši update unutar prozora
