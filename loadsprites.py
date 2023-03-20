import pygame
from rdatabase import *

class LocationSprite:
    def __init__(self, con, name):
        self.name = name
        cur = con.cursor()
        self.image = pygame.image.load(getImage(cur, name, 'Locations'))
        self.bg = pygame.image.load(getBG(cur, name))
        self.position = getOffset(cur, name)
        self.size = getLengths(cur, name)
        self.newPos = (self.position[0], self.position[1]-10)


    def showImage(self, screen):
        screen.blit(self.image, self.position)

    def bounce(self, screen):
        screen.blit(self.image, self.newPos)



