import pygame
from static_enity import StaticEntity


class Bullet(StaticEntity):
    def __init__(self, screen, setting):
        super().__init__(screen, setting, 'images/bullet.png')
        self.speed = 17

    def move(self):
        self.rect.centery -= self.speed

    def is_on_field(self):
        return self.rect.bottom >= 0
