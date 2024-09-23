import pygame
from constants import *

from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = [updatable, drawable]
    Shot.containers = [updatable, drawable, shots]
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = [updatable, drawable, asteroids]
    AsteroidField.containers = [updatable]
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collisions(player):
                print("Game over!")
                return
            for shot in shots:
                if asteroid.check_collisions(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
