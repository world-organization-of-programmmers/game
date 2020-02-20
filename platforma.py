import pygame
from static_enity import StaticEntity


class StaticPlatforma(StaticEntity):
    def __init__(self, screen, setting, image):
        super().__init__(screen, setting, image)
