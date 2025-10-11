import pygame
from constants import *
from player import *

def main():
    #init pygame
    pygame.init()
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    #checking settings
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #set player groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    players = Player(x, y)
    
    clock = pygame.time.Clock()
    dt = 0

    #set screen display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        #update all in updateable group
        updatable.update(dt)
        #draw all sprites
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()
