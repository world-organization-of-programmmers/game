import pygame


class Setting:
    def __init__(self):
        self.bg_image = pygame.image.load("images/bg.jpg")
        self.height = self.bg_image.get_rect().height
        self.width = self.bg_image.get_rect().width
        self.plt_color = (72, 73, 182)
