import pygame
from rdatabase import *

class Sprite:
    def __init__(self, con, name, table):
        self.name = name
        self.cur = con.cursor()
        self.image = pygame.image.load(getImage(self.cur, name, table))
        self.position = getOffset(self.cur, name, table)
        self.size = getLengths(self.cur, name)
        self.rect = self.image.get_rect(topleft=self.position)

    def showImage(self, screen):
        screen.blit(self.image, self.position)



class Button(Sprite):
    def __init__(self, con, name):
        super().__init__(con, name, 'Buttons')
        self.newPos = (self.position[0], self.position[1]+5)

    def bounceDown(self, screen):
        screen.blit(self.image, self.newPos)
        

class LocationSprite(Sprite):
    def __init__(self, con, name):
        super().__init__(con, name, 'Locations')
        self.bg = pygame.image.load(getBG(self.cur, name))
        self.newPos = (self.position[0], self.position[1]-10)

    def bounce(self, screen):
        screen.blit(self.image, self.newPos)



