import pygame
from pygame.locals import (
    RLEACCEL
)
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super(Enemy, self).__init__()
        self.SCREEN_WIDTH = screen_width
        self.SCREEN_HEIGHT = screen_height

        self.surf = pygame.image.load("resources/missile.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(self.SCREEN_WIDTH + 20, self.SCREEN_WIDTH + 100),
                random.randint(0, self.SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
