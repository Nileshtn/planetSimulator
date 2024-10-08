import pygame
from game_constant import GameConstant as GC
from planet import Planet
import math
pygame.init()

WIN = pygame.display.set_mode((GC.WIDTH.value,GC.HEIGHT.value))
pygame.display.set_caption("Planet Simulation")


def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0,0, 30, GC.YELLOW.value, 1.98892 * 10**30)
    sun.sun = True

    earth = Planet(-1 * Planet.AU, 0, 16, GC.BLUE.value, 5.9742e24)
    earth.y_vel = 29.783e3
    mars = Planet(-1.524 * Planet.AU, 0, 12, GC.RED.value, 6.39e23)
    mars.y_vel = 24.077e3
    mercury = Planet(-0.387* Planet.AU, 0, 8, GC.GRAY.value, 0.330e24)
    mercury.y_vel = 47.4e3
    venus = Planet(-0.723 * Planet.AU , 0, 14, GC.WHITE.value, 4.8685e24)
    venus.y_vel = 35.02e3


    planets = [sun, earth, mars, mercury, venus]

    while run:
        clock.tick(GC.FRAME_RATE.value)
        WIN.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)

        pygame.display.update()
    
    pygame.quit()


main()