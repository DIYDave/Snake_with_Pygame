import pygame
import random
import pygame_widgets
from pygame_widgets.button import Button

# Highscore: 96!!

# Konstanten
SNAKEBLOCK = 18
COLORBODY = 'green'
COLRHEAD = 'brown'
COLORAPPLE = 'red'
STARTLENGTH = 3
BACKGROUND = (180, 180, 180)
FPS  = 10
WINDOW_X = SNAKEBLOCK * 35
WINDOW_Y = SNAKEBLOCK * 26

pygame.init
pygame.font.init()
WINDOW = pygame.display.set_mode((WINDOW_X,WINDOW_Y))
pygame.display.set_caption('The Snake')
clock = pygame.time.Clock()

# Create buttons
buttonfont = pygame.font.SysFont('arial', 20)
bt_cover = Button(WINDOW,(WINDOW_X-160)/2, 50,160,40, radius=4, font = buttonfont, text = 'New Game', onClick= lambda: newgame())

class Snake():
    def __init__(self):
        self.body = []
        self.length = 0
        self.direction = None
        self.gameover = False
        self.new()

    def new(self):
        self.body = []
        for i in range(0, STARTLENGTH):
            new_body = (SNAKEBLOCK, SNAKEBLOCK * i)
            self.body.append(new_body)
        self.gameover = False
        self.direction = 'DOWN'
        self.length = len(self.body)

    def move(self):
        head = self.body[-1]
        if self.direction == 'DOWN':
            new_head = (head[0], head[1] + SNAKEBLOCK)
        if self.direction == 'UP':
            new_head = (head[0], head[1] - SNAKEBLOCK)
        if self.direction == 'RIGHT':
            new_head = (head[0] + SNAKEBLOCK, head[1])
        if self.direction == 'LEFT':
            new_head = (head[0] - SNAKEBLOCK, head[1])
        self.body.append(new_head)
        if self.length < len(self.body):
            self.body.pop(0) 

    def draw(self):
        for i in range(len(self.body)-1):
            pygame.draw.rect(WINDOW,COLORBODY,(self.body[i][0],self.body[i][1],SNAKEBLOCK,SNAKEBLOCK), border_radius = int(SNAKEBLOCK/4))
        pygame.draw.rect(WINDOW,COLRHEAD,(self.body[-1][0],self.body[-1][1],SNAKEBLOCK,SNAKEBLOCK), border_radius = int(SNAKEBLOCK/4))

    def collision(self):
        head = self.body[-1]
        for i in range(len(self.body)-1):
            if self.body[i][0] == head[0] and self.body[i][1] == head[1]:
                self.gameover = True
        if head[0] == apple.x and head[1] == apple.y:
            apple.new()
            self.length += 1
        if head[0] >= WINDOW_X or head[0] < 0:
            self.gameover = True
        if head[1] >= WINDOW_Y or head[1] < 0:
            self.gameover = True            


class Apple():
    def __init__(self):
        self.new()

    def new(self):
        block_in_x = int(WINDOW_X / SNAKEBLOCK)
        block_in_y = int(WINDOW_Y / SNAKEBLOCK)
        self.x = random.randint(0, block_in_x-1) * SNAKEBLOCK
        self.y = random.randint(0, block_in_y-1) * SNAKEBLOCK

    def draw(self):
        pygame.draw.rect(WINDOW,COLORAPPLE,(self.x,self.y,SNAKEBLOCK,SNAKEBLOCK), border_radius = int(SNAKEBLOCK/2) )
        

apple = Apple()
snake = Snake()  

def newgame():
    apple.new()
    snake.new()

def main():
    run = True
    while run:
        WINDOW.fill(BACKGROUND)
        clock.tick(FPS)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                if snake.direction != 'RIGHT':
                    snake.direction = 'LEFT'
                    break
            if keys[pygame.K_RIGHT]:
                if snake.direction != 'LEFT':
                    snake.direction = 'RIGHT'
                    break
            if keys[pygame.K_UP]:
                if snake.direction != 'DOWN':
                    snake.direction = 'UP'
                    break
            if keys[pygame.K_DOWN]:
                if snake.direction != 'UP':
                    snake.direction = 'DOWN'
                    break
        if snake.gameover:
            pygame_widgets.update(events)
        else:
            apple.draw()
            snake.move()
            snake.collision()
        snake.draw()
        caption = f'The Snake Score: {snake.length}'
        pygame.display.set_caption(caption)
        pygame.display.update()

main()    
