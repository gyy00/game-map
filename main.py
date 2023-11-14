import pygame, sys, sqlite3
from pygame.locals import *

from screens import *

#initialise pygame
pygame.init()

#sets up the game window
def initialise():
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Interactive Game Map')
    screen.fill((255, 255, 255))
    return screen
    


def main():
    screen = initialise()

    #connect to database
    con = connectData(r'database\GameData.db')

    mainMap = Map(con, screen)
    closeData(con)

    
    while True:
        #gets events, like mouse input
        for event in pygame.event.get():
            
            mainMap.showMap(screen, event)
            
            #allows closing the window
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__=='__main__':
    main()
