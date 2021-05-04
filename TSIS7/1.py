import sys, pygame, math
from pygame.locals import *

BLUE = (0,   0, 255)
WHITE = (255, 255, 255)
DARKRED = (128,   0,   0)
DARKBLUE = (0,   0, 128)
RED = (255,   0,   0)
GREEN = (0, 255,   0)
DARKGREEN = (0, 128,   0)
YELLOW = (255, 255,   0)
DARKYELLOW = (128, 128,   0)
BLACK = (0,   0,   0)

BGCOLOR = WHITE

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
WIN_CENTERX = int(WINDOWWIDTH / 2)
WIN_CENTERY = int(WINDOWHEIGHT / 2)

FPS = 160

AMPLITUDE = 100

pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Beksultan')
fontObj = pygame.font.Font('freesansbold.ttf', 16)

showSine = True
showCosine = True
pause = False

xPos = 0
step = 0
posRecord = {'sin': [], 'cos': []}

sinLabelSurf = fontObj.render('sine', True, RED, BGCOLOR)
cosLabelSurf = fontObj.render('cosine', True, BLUE, BGCOLOR)
sinLabelRect = sinLabelSurf.get_rect()
cosLabelRect = cosLabelSurf.get_rect()

instructionsSurf = fontObj.render('Press Q or W to toggle waves. P to pause.', True, BLACK, BGCOLOR)
instructionsRect = instructionsSurf.get_rect()
instructionsRect.left = 10
instructionsRect.bottom = WINDOWHEIGHT - 10

while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

        if event.type == KEYUP:
            if event.key == K_q:
                showSine = not showSine
            elif event.key == K_w:
                showCosine = not showCosine
            elif event.key == K_p:
                pause = not pause

    DISPLAYSURF.fill(BGCOLOR)

    DISPLAYSURF.blit(instructionsSurf, instructionsRect)

    pygame.draw.line(DISPLAYSURF, BLACK, (0, WIN_CENTERY), (WINDOWWIDTH, WIN_CENTERY))
    pygame.draw.line(DISPLAYSURF, BLACK, (0, WIN_CENTERY + AMPLITUDE), (WINDOWWIDTH, WIN_CENTERY + AMPLITUDE))
    pygame.draw.line(DISPLAYSURF, BLACK, (0, WIN_CENTERY - AMPLITUDE), (WINDOWWIDTH, WIN_CENTERY - AMPLITUDE))

    yPos = -1 * math.sin(step) * AMPLITUDE
    posRecord['sin'].append((int(xPos), int(yPos) + WIN_CENTERY))
    if showSine:
        pygame.draw.circle(DISPLAYSURF, RED, (int(xPos), int(yPos) + WIN_CENTERY), 10)
        sinLabelRect.center = (int(xPos), int(yPos) + WIN_CENTERY + 20)
        DISPLAYSURF.blit(sinLabelSurf, sinLabelRect)

    yPos = -1 * math.cos(step) * AMPLITUDE
    posRecord['cos'].append((int(xPos), int(yPos) + WIN_CENTERY))
    if showCosine:
        pygame.draw.circle(DISPLAYSURF, BLUE, (int(xPos), int(yPos) + WIN_CENTERY), 10)
        cosLabelRect.center = (int(xPos), int(yPos) + WIN_CENTERY + 20)
        DISPLAYSURF.blit(cosLabelSurf, cosLabelRect)

    if showSine:
        for x, y in posRecord['sin']:
            pygame.draw.circle(DISPLAYSURF, DARKRED, (x, y), 4)
    if showCosine:
        for x, y in posRecord['cos']:
            pygame.draw.circle(DISPLAYSURF, DARKBLUE, (x, y), 4)

    pygame.draw.rect(DISPLAYSURF, BLACK, (0, 0, WINDOWWIDTH, WINDOWHEIGHT), 1)

    pygame.display.update()
    FPSCLOCK.tick(FPS)

    if not pause:
        xPos += 0.5
        if xPos > WINDOWWIDTH:
            xPos = 0
            posRecord = {'sin': [], 'cos': []}
            step = 0
        else:
            step += 0.008
            step %= 2 * math.pi

