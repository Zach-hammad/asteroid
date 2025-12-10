from circleshape import CircleShape
import pygame
from constants import *
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            movement1 = self.velocity.rotate(angle)
            movement2 = self.velocity.rotate(-angle)
            radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, radius)
            asteroid1.velocity = movement1 * 1.2
            asteroid2.velocity = movement2 * 1.2
