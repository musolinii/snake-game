class Menu:
     def show_menu(self):
        self.surface.fill((5,5,5))
        font = pygame.font.SysFont('arial',30)
        message1 = font.render("Welcome to Snake !",True,(255,255,255))
        self.surface.blit(message1,(200,200))
        message2 = font.render("Enter your name",True,(255,255,255))
        self.surface.blit(message2,(200,250))
        pygame.display.flip()
    