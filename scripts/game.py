import pygame
import os

class Game():
    def __init__(self):
        self.background = pygame.display.set_icon(pygame.image.load(os.path.join("assets","icons","icon.ico")))
    def render(self,surface: pygame.Surface):
        surface.blit(self.background, (0,0))        #взяла у дениса-лучшего на всём белом свете лоха
