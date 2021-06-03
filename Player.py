import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    RLEACCEL
)


class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, move_up_sound, move_down_sound):
        super(Player, self).__init__()
        self.SCREEN_WIDTH = screen_width
        self.SCREEN_HEIGHT = screen_height

        self.surf = pygame.image.load("resources/jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                20 + self.surf.get_width()/2,
                (self.SCREEN_HEIGHT - self.surf.get_height())/2,
            )
        )

        self.move_up_sound = move_up_sound
        self.move_down_sound = move_down_sound

    def update(self, pressed_player_keys):
        if pressed_player_keys[K_UP]:
            self.rect.move_ip(0, -5)
            self.move_up_sound.play()
        if pressed_player_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            self.move_down_sound.play()
        if pressed_player_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_player_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.SCREEN_WIDTH:
            self.rect.right = self.SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.SCREEN_HEIGHT:
            self.rect.bottom = self.SCREEN_HEIGHT
