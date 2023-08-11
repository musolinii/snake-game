import pygame
from pygame.locals import *





SIZE = 20

class Snake:
    def __init__(self,parent_screen,length):
        self.length = length
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/snake.png").convert()
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.direction = 'right'

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))
            self.DEFAULT_IMAGE_SIZE = (20, 20)
            self.image = pygame.transform.scale(self.image, self.DEFAULT_IMAGE_SIZE)

        pygame.display.flip()
        
    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'
    
    def crawl(self):

        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        
        if self.direction == 'up':
            self.y[0] -= 20
            
        if self.direction == 'down':
            self.y[0] += 20

        if self.direction == 'left':
            self.x[0] -= 20

        if self.direction == 'right':
            self.x[0] += 20

        self.draw()
