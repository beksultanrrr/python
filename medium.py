import pygame
import random
import time

pygame.init()

pygame.font.init()

screen_size = (1080, 720)
screen = pygame.display.set_mode(screen_size)
background = pygame.transform.scale(pygame.image.load("snake1.png"),(screen_size))
barrier=pygame.transform.scale(pygame.image.load("grey_brick_state_1_center_repeating.png"),(40,75))
barrier1=pygame.transform.scale(pygame.image.load("grey_brick_state_1_left_side.png"),(50,85))
barrier2=pygame.transform.scale(pygame.image.load("grey_brick_state_1_right_side.png"),(45,85))
IMAGE = pygame.image.load("grey_brick_state_1_center_repeating.png").convert()
rect = IMAGE.get_rect()
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255,255,0)
rect.center = (200, 300)
pygame.display.set_caption('Змейка')
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
FPS = 90
d = 3

score=0
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

FONT = pygame.font.SysFont('Arial', 60)
running = True

color_change1 = random.randint(0, 255)
color_change2 = random.randint(0, 255)
color_change3 = random.randint(0, 255)
brown = ((100,40,0))

class Snake:
    def __init__(self):
        self.size = 1
        self.elements = [[100, 100]]
        self.radius = 10
        self.dx = d
        self.dy = 0
        self.grow = False
        self.dir = 'right'
        self.need_to_grow = 5

    def draw(self):

        for element in self.elements[1:]:
            color_change1 = random.randint(0, 255)
            color_change2 = random.randint(0, 255)
            color_change3 = random.randint(0, 255)
            pygame.draw.circle(screen, (color_change1, color_change2, color_change3), element, self.radius)

        pygame.draw.circle(screen, (255, 255, 255), (self.elements[0][0], self.elements[0][1]), self.radius)

    def move(self):
        global running
        if self.need_to_grow > 0:
            self.need_to_grow -= 1
            self.grow = True

        self.elements.insert(0, [self.elements[0][0] + self.dx, self.elements[0][1] + self.dy])

        if not self.grow:
            self.elements.pop()
        else:
            self.grow = False
            self.size += 1

        if self.elements[0] in self.elements[1:]:
            running = False


class Fruit:

    def __init__(self):
        self.radius = 10
        self.generate()

    def draw(self):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius)

    def generate(self):
        global snake
        self.x = random.randint(10, screen_size[0] - 40)
        self.y = random.randint(10, screen_size[1] - 40)

        for i in range(snake.size):
            if (abs(snake.elements[i][0] - self.x) <= self.radius + snake.radius and abs(
                    snake.elements[i][1] - self.y) <= self.radius + snake.radius):
                self.generate()


snake = Snake()
fruit = Fruit()
clock = pygame.time.Clock()

while running:
    screen.blit(background, (0, 0))
    screen.blit(barrier, (540, 340))
    screen.blit(barrier, (580, 340))
    screen.blit(barrier, (620, 340))
    screen.blit(barrier, (660, 340))
    screen.blit(barrier, (700, 340))
    screen.blit(barrier, (720, 340))
    screen.blit(barrier, (760, 340))
    screen.blit(barrier, (800, 340))
    screen.blit(barrier, (500, 340))
    screen.blit(barrier, (460, 340))
    screen.blit(barrier, (420, 340))
    screen.blit(barrier, (380, 340))
    screen.blit(barrier, (340, 340))
    screen.blit(barrier, (300, 340))
    screen.blit(barrier, (260, 340))
    pygame.draw.rect(screen, (brown),
                     (0, 0, 1080, 720), 30)

    scores1 = font_small.render("score=" + str(score), True, RED)
    screen.blit(scores1, (900, 30))
    Ticks = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_LEFT and snake.dir != 'right':
                snake.dx = -d
                snake.dy = 0
                snake.dir = 'left'
            if event.key == pygame.K_RIGHT and snake.dir != 'left':
                snake.dx = d
                snake.dy = 0
                snake.dir = 'right'
            if event.key == pygame.K_UP and snake.dir != 'down':
                snake.dx = 0
                snake.dy = -d
                snake.dir = 'up'
            if event.key == pygame.K_DOWN and snake != 'up':
                snake.dx = 0;
                snake.dy = d
                snake.dir = 'down'
            if event.key == pygame.K_1:
                snake.need_to_grow = 5

    if snake.elements[0][0] < 0 or snake.elements[0][0] > 1080 - 30:
        screen.fill(RED)
        screen.blit(game_over, (350, 350))
        time.sleep(1)
    if snake.elements[0][0] < 30:
        screen.fill(RED)
        screen.blit(game_over, (350, 350))
        time.sleep(1)
    if snake.elements[0][1] < 0 or snake.elements[0][1] > 720 - 30:
        screen.fill(RED)
        screen.blit(game_over, (350, 350))
        time.sleep(1)
    if snake.elements[0][1] <30:
        screen.fill(RED)
        screen.blit(game_over, (350, 350))
        time.sleep(1)

    if 540 < snake.elements[0][0] < 580 and 340 < snake.elements[0][1] < 415:
        screen.fill(RED)
        screen.blit(game_over, (350, 350))
        time.sleep(1)
    if 580 < snake.elements[0][0] < 620 and 340 < snake.elements[0][1] < 415:
        screen.fill(RED)
        screen.blit(game_over, (350, 350))
        time.sleep(1)
    if 620 < snake.elements[0][0] < 640 and 340 < snake.elements[0][1] < 415:
        screen.fill(RED)
        screen.blit(game_over, (350, 350))
        time.sleep(1)
    if 660 < snake.elements[0][0] < 700 and 340 < snake.elements[0][1] < 415:
        screen.fill(RED)
        screen.blit(game_over, (350, 350))
        time.sleep(1)
    if 720 < snake.elements[0][0] < 760 and 340 < snake.elements[0][1] < 415:
        screen.fill(RED)
        screen.blit(game_over, (350, 350))
        time.sleep(1)
    if 760 < snake.elements[0][0] < 800 and 340 < snake.elements[0][1] < 415:
        screen.fill(RED)
        screen.blit(game_over, (350, 350))
        time.sleep(1)
    if 800 < snake.elements[0][0] < 840 and 340 < snake.elements[0][1] < 415:
        screen.fill(RED)
        screen.blit(game_over, (350, 350))
        time.sleep(1)
    if 500 < snake.elements[0][0] < 540 and 340 < snake.elements[0][1] < 415:
        screen.fill(RED)
        screen.blit(game_over, (350, 350))
        time.sleep(1)
    if 460 < snake.elements[0][0] < 500 and 340 < snake.elements[0][1] < 415:
        screen.fill(RED)
        screen.blit(game_over, (350, 350))
        time.sleep(1)
    if 420 < snake.elements[0][0] < 460 and 340 < snake.elements[0][1] < 415:
        screen.fill(RED)
        screen.blit(game_over, (350, 350))
        time.sleep(1)
    if 380 < snake.elements[0][0] < 420 and 340 < snake.elements[0][1] < 415:
        screen.fill(RED)
        screen.blit(game_over, (350, 350))
        time.sleep(1)
    if 340 < snake.elements[0][0] < 380 and 340 < snake.elements[0][1] < 415:
        screen.fill(RED)
        screen.blit(game_over, (350, 350))
        time.sleep(1)
    if 300 < snake.elements[0][0] < 340 and 340 < snake.elements[0][1] < 415:
        screen.fill(RED)
        screen.blit(game_over, (350, 350))
        time.sleep(1)
    if 260 < snake.elements[0][0] < 300 and 340 < snake.elements[0][1] < 415:
        screen.fill(RED)
        screen.blit(game_over, (350, 350))
        time.sleep(1)



    #4075
    if (abs(snake.elements[0][0] - fruit.x) <= (fruit.radius + snake.radius) and abs(
            snake.elements[0][1] - fruit.y) <= (fruit.radius + snake.radius)):
        snake.need_to_grow = 5
        fruit.generate()
        score +=1


    snake.move()
    snake.draw()
    fruit.draw()
    pygame.display.flip()




