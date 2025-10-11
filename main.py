import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    #init pygame
    pygame.init()
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    #checking settings
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #set groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
   

    #set up containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    #init objects
    asteroid_field = AsteroidField()
    players = Player(x, y)

    clock = pygame.time.Clock()
    dt = 0

    #set screen display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(BLACK)
        #update all in updateable group
        updatable.update(dt)
        #draw all sprites
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()
