##This file assembles the map and different areas of the game

import pygame
from loadsprites import *

class Map:
    def __init__(self, con, screen):
        self.bg = pygame.image.load('images/backgrounds/village.png')
        self.farm = LocationSprite(con, 'Rainbow Farm')
        self.void = LocationSprite(con, 'The Void')
        self.lake = LocationSprite(con, 'Magical Lake')
        self.currentLocation = 'Main Map'

        self.back = Button(con, 'Back')


    def showMap(self, screen, event):

        #display certain assets depending on the current location of the player
        if self.currentLocation == 'Main Map':
            screen.blit(self.bg, (0, 0))
            self.farm.showImage(screen)
            self.void.showImage(screen)
            self.lake.showImage(screen)


            #check if mouse is hovering over a location
            if self.farm.rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(self.bg, (0, 0))
                self.farm.bounce(screen)
                self.void.showImage(screen)
                self.lake.showImage(screen)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.currentLocation = self.farm.name

            elif self.void.rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(self.bg, (0, 0))
                self.void.bounce(screen)
                self.farm.showImage(screen)
                self.lake.showImage(screen)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.currentLocation = self.void.name

            elif self.lake.rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(self.bg, (0, 0))
                self.lake.bounce(screen)
                self.farm.showImage(screen)
                self.void.showImage(screen)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.currentLocation = self.lake.name
            

        elif self.currentLocation == self.farm.name:
            #display farm background and back button
            #if back button is clicked, go back to main map
            
            screen.blit(self.farm.bg, (0, 0))
            self.back.showImage(screen)

            if self.back.image.get_rect(topleft=self.back.position).collidepoint(pygame.mouse.get_pos()):
                screen.blit(self.farm.bg, (0, 0))
                self.back.bounceDown(screen)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.currentLocation = 'Main Map'
            

        elif self.currentLocation == self.void.name:
            #display void background and back button
            #if back button is clicked, go back to main map
            
            screen.blit(self.void.bg, (0, 0))
            self.back.showImage(screen)
            
            if self.back.image.get_rect(topleft=self.back.position).collidepoint(pygame.mouse.get_pos()):
                screen.blit(self.void.bg, (0, 0))
                self.back.bounceDown(screen)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.currentLocation = 'Main Map'
            

        elif self.currentLocation == self.lake.name:
            #display lake background and back button
            #if back button is clicked, go back to main map
            
            screen.blit(self.lake.bg, (0, 0))
            self.back.showImage(screen)
            
            if self.back.image.get_rect(topleft=self.back.position).collidepoint(pygame.mouse.get_pos()):
                screen.blit(self.lake.bg, (0, 0))
                self.back.bounceDown(screen)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.currentLocation = 'Main Map'
            

        ##Note: flip() is faster than update() when double buffering
        ##       i.e. making lots of changes to the screen
        ##      Flip pushes the frame at once when everything is drawn.
        pygame.display.flip()

