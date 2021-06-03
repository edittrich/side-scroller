import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

from Cloud import Cloud as Cloud
from Enemy import Enemy as Enemy
from Player import Player as Player


pygame.mixer.init()
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.mixer.music.load("resources/background.mp3")
pygame.mixer.music.play(loops=-1)

move_up_sound = pygame.mixer.Sound("resources/rising_putter.ogg")
move_down_sound = pygame.mixer.Sound("resources/falling_putter.ogg")
collision_sound = pygame.mixer.Sound("resources/collision.ogg")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, 250)
ADD_CLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADD_CLOUD, 1000)

player = Player(SCREEN_WIDTH, SCREEN_HEIGHT, move_up_sound, move_down_sound)
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

        elif event.type == ADD_ENEMY:
            new_enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        elif event.type == ADD_CLOUD:
            new_cloud = Cloud(SCREEN_WIDTH, SCREEN_HEIGHT)
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    enemies.update()
    clouds.update()

    screen.fill((135, 206, 250))

    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        running = False

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip()

    clock.tick(30)

pygame.mixer.music.stop()
move_up_sound.stop()
move_down_sound.stop()
collision_sound.play()

pygame.time.wait(int(collision_sound.get_length() * 1000))

pygame.mixer.quit()
pygame.quit()
