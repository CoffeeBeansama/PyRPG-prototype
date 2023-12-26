import pygame, sys
from settings import *
from level import Level
from player import * 
from Buttons import *
from debug import  debug

class Game:		
    def __init__(self):
          
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))

        pygame.display.set_caption("Game Zelda Prototype")
        self.clock = pygame.time.Clock()
        self.level = Level()
     
    def run(self):
        while True:
        
            for event in pygame.event.get():
            
               if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.level.run() 	
            pygame.display.update()
            self.clock.tick(FPS)
     
  
if __name__ == '__main__':

    game = Game()
    game.run()
