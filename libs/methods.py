import pygame
import os
from pygame.locals import *

'''
Restart or Quit Logic
'''
def replay_or_quit():
    for event in pygame.event.get([pygame.JOYBUTTONDOWN, pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.JOYBUTTONDOWN:
            continue

        return event.key
    
    return None


'''
Load an image from the data directory with per pixel alpha transparency.
'''
def load_image(i):
    return pygame.image.load(os.path.join("Data", i)).convert_alpha()

''' 
Return Text Area
'''
def makeTextObjs(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

'''
Add Game Over Message and restart logic
'''
def msgSurface(text):
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    largeText = pygame.font.Font('freesansbold.ttf', 150)

    titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
    titleTextRect.center = surfaceWidth / 2, surfaceHeight / 2
    surface.blit(titleTextSurf, titleTextRect)

    typTextSurf, typTextRect = makeTextObjs('Press any key to continue', smallText)
    typTextRect.center =  surfaceWidth / 2, ((surfaceHeight / 2) + 100)
    surface.blit(typTextSurf, typTextRect)

    pygame.display.update()
    #time.sleep(1)

    while replay_or_quit() == None:
        clock.tick()

    main()

def score(count):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render("Score: "+str(count), True, black)
    surface.blit(text, [10,10])    
    
def lives(lcount):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render("Lives: "+str(lcount), True, black)
    surface.blit(text, [surfaceWidth-100,10])    

def showBombs(bcount):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render("Bombs: "+str(bcount), True, black)
    surface.blit(text, [450,10])    

def die(explode, rect):
    surface.blit(explode, rect)
    pygame.display.update(rect)
    
def gameOver():
    msgSurface('Game Over')

def test(i, x, y):
    font = pygame.font.Font('freesansbold.ttf', 20)
    smfont = pygame.font.Font('freesansbold.ttf', 10)
    herotext = font.render("x:" + str(x) + " y:"+str(y), True, black)
    countertext = font.render("i:" + str(i) , True, black)
    one = smfont.render("100", True, black)
    three = smfont.render("300", True, black)
    five = smfont.render("500", True, black)
    seven = smfont.render("700", True, black)
    surface.blit(herotext, [400,30])
    surface.blit(countertext, [400,50])
    surface.blit(one, [100,5])
    surface.blit(one, [5,100])
    surface.blit(one, [970,100])
    surface.blit(one, [100,690])
    surface.blit(three, [300,5])
    surface.blit(three, [5,300])
    surface.blit(three, [970,300])
    surface.blit(three, [300,690])
    surface.blit(five, [500,5])
    surface.blit(five, [5,500])
    surface.blit(five, [970,500]) 
    surface.blit(five, [500,690])   
    surface.blit(seven, [700,5])
    surface.blit(seven, [700,690])
