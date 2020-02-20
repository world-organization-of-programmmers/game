import pygame
from hero import Hero
from random import randint
import game_function as gf
from setting import Setting
from static_enity import StaticEntity

setting = Setting()

pygame.init()

screen = pygame.display.set_mode((setting.width, setting.height))

doodle = Hero(screen, setting, 'images/stay.png')

doodle.start_position([setting.width / 2, setting.height - doodle.rect.height * 5])
platforms = []
for i in range(5):
    plt = StaticEntity(screen, setting, 'images/block.png')
    plt.start_position([randint(0, setting.width - plt.rect.width), setting.height / 6 * i + plt.rect.height])

    platforms.append(plt)

plt = StaticEntity(screen, setting, 'images/block.png')
plt.start_position()
platforms.append(plt)

while True:
    gf.check_events(doodle)
    doodle.move()

    doodle.move_y(platforms)
    doodle.animation(platforms)

    screen.blit(setting.bg_image, (0, 0))
    for plt in platforms:
        plt.blit()

    doodle.shoot()
    doodle.blit()

    pygame.display.flip()
    pygame.time.delay(24)
