# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    dt = 0
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    player = Player(x,y)
    asteriod_field = AsteroidField()
    running = True
    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False

        for thing in updatable:
            thing.update(dt)

        for asteroid in asteroids:
            if asteroid.detect_collision(player):
                print("Game over!")
                running = False

        screen.fill("black")

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()