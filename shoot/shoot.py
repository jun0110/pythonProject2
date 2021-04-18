import pygame
import sys
import random
from time import sleep

padWidth = 480
padHeight = 640
rockImage = ['rock01.png', 'rock02.png', 'rock03.png', 'rock04.png', 'rock05.png',
             'rock06.png', 'rock07.png', 'rock08.png', 'rock09.png', 'rock10.png',
             'rock11.png', 'rock12.png', 'rock13.png', 'rock14.png', 'rock15.png',
             'rock16.png', 'rock17.png', 'rock18.png', 'rock19.png', 'rock20.png',
             'rock21.png', 'rock22.png', 'rock23.png', 'rock24.png', 'rock25.png',
             'rock26.png', 'rock27.png', 'rock28.png', 'rock29.png', 'rock30.png']

def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x, y))

def initGame():
    global gamePad, clock, background, fighter, missile, explosion
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('shoot')
    background = pygame.image.load('background.png')
    fighter = pygame.image.load('fighter.png')
    missile = pygame.image.load('missile.png')
    explosion = pygame.image.load('explosion.png')
    clock = pygame.time.Clock

def runGame():
    global gamepad, clock, background, fighter, missile, explosion

    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeiget = fighterSize[1]

    x = padWidth * 0.45
    y = padHeight * 0.9
    fighterX = 0

    missileXY = []

    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size
    rockWidth = rockSize[0]
    rockHight = rockSize[1]

    rockX = random.randrange(0, padWidth - rockWidth)
    rockY = 0
    rockSpeed = 2

    isShot = False
    shotCount = 0
    rockPassed = 0

    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT:
                    fighterX -= 5

                elif event.key == pygame.K_RIGHT:
                    fighterX +=5

                elif event.key == pygame.K_SPACE:
                    missileX = x + fighterWidth/2
                    missileY = y - fighterHeiget
                    missileXY.append([missileX, missileY])

            if event.type in [pygame.KEYUP]:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighterX = 0


        drawObject(background, 0, 0)

        x += fighterX
        if x < 0:
            x = 0
        elif x > padWidth - fighterWidth:
            x = padWidth - fighterWidth

        drawObject(fighter, x, y)

        if len(missileXY) != 0:
            for i, bxy in enumerate(missileXY):
                bxy[1] -= 10
                missileXY[i][1] = bxy[1]

                if bxy[1] <= 0:
                    try:
                        missileXY.remove(bxy)
                    except:
                        pass

        if len(missileXY) != 0:
            for bx, by in missileXY:
                drawObject(missile, bx, by)

        rockY += rockSpeed

        if rockY > padHeight:
            rock = pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size
            rockWidth = rockSize[0]
            rockHight = rockSize[1]
            rockX = random.randrange(0, padWidth - rockWidth)
            rockY = 0

        drawObject(rock, rockX, rockY)

        pygame.display.update()

        clock().tick(60)

    pygame.quit()

initGame()
runGame()