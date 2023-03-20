##This file assembles the map and different areas of the game

import pygame
from loadsprites import *

class Map:
    def __init__(self, con, screen):
        self.bg = pygame.image.load('images/backgrounds/village.png')
        self.farm = LocationSprite(con, 'Rainbow Farm')
        self.void = LocationSprite(con, 'The Void')
        self.lake = LocationSprite(con, 'Magical Lake')



    def showMap(self, screen):
        screen.blit(self.bg, (0, 0))
        self.farm.showImage(screen)
        self.void.showImage(screen)
        self.lake.showImage(screen)
        self.updateNeeded = 0

        #check if mouse is hovering over a location
        if self.farm.image.get_rect(topleft=self.farm.position).collidepoint(pygame.mouse.get_pos()):
            screen.blit(self.bg, (0, 0))
            self.farm.bounce(screen)
            self.void.showImage(screen)
            self.lake.showImage(screen)

        elif self.void.image.get_rect(topleft=self.void.position).collidepoint(pygame.mouse.get_pos()):
            screen.blit(self.bg, (0, 0))
            self.void.bounce(screen)
            self.farm.showImage(screen)
            self.lake.showImage(screen)

        elif self.lake.image.get_rect(topleft=self.lake.position).collidepoint(pygame.mouse.get_pos()):
            screen.blit(self.bg, (0, 0))
            self.lake.bounce(screen)
            self.farm.showImage(screen)
            self.void.showImage(screen)
            

        ##Note: flip() is faster than update() when double buffering
        ##       i.e. making lots of changes to the screen
        ##      It pushes the frame at once when everything is drawn.
        pygame.display.flip()




