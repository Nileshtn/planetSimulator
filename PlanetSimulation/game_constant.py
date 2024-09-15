from enum import Enum
import pygame
pygame.init()

class GameConstant(Enum):
    WIDTH, HEIGHT = 800, 800
    FRAME_RATE = 60
    FONT = pygame.font.SysFont("arial", 16)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    GRAY = (124, 124, 124)
    WHITE = (255, 255, 255)