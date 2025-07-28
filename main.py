import pygame
from asteroidfield import AsteroidField  
from constants import *
from player import Player
from asteroid import Asteroid

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("py_roids")
    clock = pygame.time.Clock()

    # Creating groups 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    # setting Containers of action to defined groups
    Player.containers = (updatable, drawable) 
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH /2 , SCREEN_HEIGHT /2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        
        screen.fill("black")
        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000
        
if __name__ == "__main__":
    main()
