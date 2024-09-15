from game_constant import GameConstant as GC
import pygame

class Planet:
    AU = 149.6e6 * 1000
    G = 6.6743e-11
    SCALE = 250/AU
    TIMESTEP = 3600 * 24

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.sun = False
        self.distance_to_sun = 0
        self.orbit = []

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = (self.x * self.SCALE) + (GC.WIDTH.value / 2)
        y = (self.y * self.SCALE) + (GC.HEIGHT.value / 2)
        pygame.draw.circle(win, self.color,(x,y),self.radius)