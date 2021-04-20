import pygame
from os import system

pygame.init()

screeen = pygame.display.set_mode((1080, 720))

font1 = pygame.font.SysFont("Verdana", 40)
font = pygame.font.SysFont("Verdana", 20)

BG = pygame.image.load('zmeyka.jpg')
BG = pygame.transform.scale(BG, (1080, 720))


def buttons(ok):
    easy = pygame.Rect(50, 600, 270, 80)
    medium = pygame.Rect(405, 600, 270, 80)
    hard = pygame.Rect(750, 600, 270, 80)

    a, b = pygame.mouse.get_pos()

    if easy.collidepoint(a,b ) and ok:
        system('easy.py')
    if medium.collidepoint(a,b) and ok:
        system('medium.py')
    if hard.collidepoint(a,b ) and ok:
        system('hard.py')


def draw():
    screeen.blit(BG, (0, 0))

    screeen.blit(font1.render('TSIS 9 by Beksultan', True, (0, 0, 0)), (30, 30))
    screeen.blit(font1.render('Snake game :D', True, (0, 0, 0)), (30, 100))
    screeen.blit(font1.render('Welcome! Choose you level', True, (0, 0, 0)), (160, 250))
    screeen.blit(font1.render("and LET'S GO", True,(0, 0, 0)), (320, 320))

    screeen.blit(font.render('level 1 (1 player)', True, (0, 0, 0)), (100, 630))
    screeen.blit(font.render('level 2 (1 player)', True, (0, 0, 0)), (450, 630))
    screeen.blit(font.render('level 3 (2 player)', True, (0, 0, 0)), (790, 630))

    pygame.draw.rect(screeen,  (255, 0, 0), [50, 600, 270, 80], 4)
    pygame.draw.rect(screeen,  (255, 0, 0), [405, 600, 270, 80], 4)
    pygame.draw.rect(screeen,  (255, 0, 0), [750, 600, 270, 80], 4)


def main():
    running = True
    button = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                button = True

        draw()
        buttons(button)
        pygame.display.update()
        button = False

    pygame.quit()


main()
