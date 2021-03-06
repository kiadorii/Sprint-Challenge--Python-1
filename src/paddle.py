import pygame

from pygame.math import Vector2
from pygame import Rect

class Paddle:
    """
    Base class for Paddle
    """

    def __init__(self, position, width, height, color):
        # Create a rectangle centered around the x and y
        self.position = position
        self.width = width
        self.rectangle = pygame.Rect(
                                    position.x - (width/2),
                                    position.y - (height/2),
                                    width,
                                    height)
        self.color = color
        self.touched_by_ball = False

    def update(self, **kwargs):
        self.touched_by_ball = False

        mouse_pos = pygame.mouse.get_pos()
        self.position.x = mouse_pos[0]
        self.rectangle[0] = mouse_pos[0] - self.width / 2

    def check_collision(self):
        pass

    def draw(self, screen, pygame):
        pygame.draw.rect(screen, self.color, self.rectangle)

class KineticPaddle(Paddle):
    # No custom code needed here, just want to be able to differentiate
    # KineticBall will handle the collison 
    pass