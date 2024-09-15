from game_constant import GameConstant as GC
import pygame
import math


class Planet:
    AU = 149.6e6 * 1000
    G = 6.6743e-11
    SCALE = 220/AU
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

    def draw(self, win:pygame.surface):
        x = (self.x * self.SCALE) + (GC.WIDTH.value / 2)
        y = (self.y * self.SCALE) + (GC.HEIGHT.value / 2)
        if len(self.orbit) > 2:
            updated_point = []
            for point in self.orbit:
                orbit_x,orbit_y = point
                orbit_x = orbit_x * self.SCALE + GC.WIDTH.value/2 
                orbit_y = orbit_y * self.SCALE + GC.HEIGHT.value/2 
                updated_point.append((orbit_x,orbit_y))

            pygame.draw.lines(win, self.color, False, updated_point, 2)

        if not self.sun:
            distance_text = GC.FONT.value.render(f"{(self.distance_to_sun/1000):.1f}Km",
                                                  1, 
                                                  GC.WHITE.value)
            win.blit(distance_text, (x - distance_text.get_width()/2,
                                     y - self.radius - distance_text.get_height()))
        pygame.draw.circle(win, self.color,(x,y),self.radius)

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x**2 + distance_y**2)

        if other.sun:
            self.distance_to_sun = distance

        force = self.G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)

        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        return force_x, force_y
    
    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self ==  planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP

        self.orbit.append((self.x, self.y))