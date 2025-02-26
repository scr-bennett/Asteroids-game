import pygame
from constants import *
from player import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = (updateables, drawables)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0)) 
        updateables.update(dt)
        for drawable in drawables:
            drawable.draw(screen)
         
        
               
        pygame.display.flip()
        

        
        
        dt = clock.tick(60) / 1000

        
if __name__ == "__main__":
    main()