import pygame
import random



SIZE = 20


class Apple:
    def __init__(self,parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/apple.jpeg").convert()
        self.DEFAULT_IMAGE_SIZE = (20, 20)
        self.image = pygame.transform.scale(self.image, self.DEFAULT_IMAGE_SIZE)
        self.x = SIZE
        self.y = SIZE
    
    def draw(self):
            self.parent_screen.blit(self.image, (self.x, self.y))
            self.DEFAULT_IMAGE_SIZE = (20, 20)
            self.image = pygame.transform.scale(self.image, self.DEFAULT_IMAGE_SIZE)
            pygame.display.flip()

    def move(self):
        self.x = random.randint(0,40)*SIZE
        self.y = random.randint(0,20)*SIZE

