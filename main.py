import pygame
from constants import *
from logger import log_state
from player import *

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    FPS = 60
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    
    
    #this is to hold everything that has to be updated in the game
    updatable = pygame.sprite.Group()
    
    #this is to hold everything that has to be drawn in the game
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    player = Player( SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while running:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
       
        dt = clock.tick(FPS) / 1000



if __name__ == "__main__":
    main()
