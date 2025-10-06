import pygame
from constants import *

def main():
    #init pygame
    pygame.init()

    #checking settings
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #set screen display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = True
    while x: 
        screen.fill((0,0,0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
