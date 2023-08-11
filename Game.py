import pygame
from Snake import Snake
from Apple import Apple
import time
from pygame.locals import *


SIZE = 20


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000,500))
        self.surface.fill((5,5,5))
        self.snake = Snake(self.surface,19)
        self.apple = Apple(self.surface)
    
    def show_menu(self):
        self.surface.fill((5,5,5))
        font = pygame.font.SysFont('arial',30)
        message1 = font.render("Welcome to Snake Game!",True,(255,255,255))
        self.surface.blit(message1,(200,200))
        message2 = font.render("To play press enter, to quit press escape.",True,(255,255,255))
        self.surface.blit(message2,(200,250))
        message3 = font.render("Press E for Easy, M for Medium and H for hard.",True,(255,255,255))
        self.surface.blit(message3,(200,300))
        pygame.display.flip()
    
    def score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render("Score: "+str(self.snake.length),True,(255,255,255))
        self.surface.blit(score,(10,10))

    def play(self):
        self.snake.crawl()
        self.apple.draw()

        if self.collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
            self.snake.increase_length()
            self.apple.move()

        self.score()
        pygame.display.flip()

        for i in range(3,self.snake.length):
            if self.collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
               raise "Game over"

    def show_game_over(self):
        self.surface.fill((5,5,5))
        font = pygame.font.SysFont('arial',30)
        message1 = font.render("Game over! Your score is "+str(self.snake.length),True,(255,255,255))
        self.surface.blit(message1,(200,200))
        message2 = font.render("To play again press enter, to quit press escape.",True,(255,255,255))
        self.surface.blit(message2,(200,250))
        pygame.display.flip()

    def pause(self):
        self.surface.fill((5,5,5))
        font = pygame.font.SysFont('arial',30)
        message1 = font.render("Paused",True,(255,255,255))
        self.surface.blit(message1,(200,200))
        message2 = font.render("To continue again press P, to quit press escape.",True,(255,255,255))
        self.surface.blit(message2,(200,250))
        pygame.display.flip()
    
    def run (self):
         
        running = True
        end = False
        pause = False
        check = False
        mode = 0.05

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        end = False
                    if event.key == K_ESCAPE:
                        running = False
                    if not end:
                        if event.key == K_BACKSPACE:
                            self.pause()
                            pause = True
                        if event.key == K_p:
                            pause = False
                        if not pause:
                            if event.key ==K_UP:
                                self.snake.move_up()
                            if event.key ==K_DOWN:
                                self.snake.move_down()
                            if event.key ==K_LEFT:
                                self.snake.move_left()
                            if event.key ==K_RIGHT:
                                self.snake.move_right()    

                elif event.type == QUIT:
                    running = False
            try:
                if not end:
                    if not pause:
                        if not check:
                            self.show_menu()
                        if event.type == KEYDOWN:
                            if event.key == K_RETURN:
                                check = True                         
                        if check: 
                            self.play()
            except Exception as e:
                self.show_game_over()
                end = True
                self.reset()

            time.sleep(mode)

    def collision(self,x1,y1,x2,y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def reset(self):
        self.snake = Snake(self.surface,2)
        self.apple = Apple(self.surface)


    