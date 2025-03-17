# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main ():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        for item in drawable:
            item.draw(screen)
        for item in updatable:
            item.update(dt)
        for item in asteroids:
            if item.check_collision(player):
                print("Game Over!")
                sys.exit()
        for item in asteroids:
            for shot in shots:
                if item.check_collision(shot):
                    item.split()
                    shot.kill()

        pygame.display.flip()

        dt = clock.tick(FPS) / 1000

if __name__ == "__main__":
    main()