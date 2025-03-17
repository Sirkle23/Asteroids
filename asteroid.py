import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rand_angle = random.uniform(MIN_RAND_ANGLE, MAX_RAND_ANGLE)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        first_asteroid = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        first_asteroid.velocity = self.velocity.rotate(rand_angle) * ASTEROID_SPEEDUP
        second_asteroid = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        second_asteroid.velocity = self.velocity.rotate(-rand_angle) * ASTEROID_SPEEDUP

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, DEF_ASTEROID_RADIUS)