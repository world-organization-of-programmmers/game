import pygame
from static_enity import StaticEntity


class Entity(StaticEntity):
    def __init__(self, screen, setting, image):
        super().__init__(screen, setting, image)
        self.speed_x = 16
        self._move_right_f = False
        self._move_left_f = False

    def _move_right(self):
        if self.rect.right <= self.setting.width:
            self.rect.centerx += self.speed_x
        else:
            self.rect.centerx = 0

    def _move_left(self):
        if self.rect.left >= 0:
            self.rect.centerx -= self.speed_x
        else:
            self.rect.centerx = self.setting.width

    def move(self):
        if self._move_left_f:
            self._move_left()
        if self._move_right_f:
            self._move_right()
