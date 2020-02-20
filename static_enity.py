import pygame


class StaticEntity:
    def __init__(self, screen, setting, image=None):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.screen = screen
        self.setting = setting

    def start_position(self, position=None):
        if position is None:
            position = [self.setting.width / 2 - self.rect.width / 2, self.setting.height - self.rect.height]
        self.rect.top = position[1]
        self.rect.left = position[0]

    def blit(self):
        self.screen.blit(self.image, self.rect)
