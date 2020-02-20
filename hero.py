import pygame
from entity import Entity
from static_enity import StaticEntity
from bullet import Bullet


class Hero(Entity):
    def __init__(self, screen, setting, image):
        super().__init__(screen, setting, image)
        self.speed_y = 0
        self._moment_speed_y = 0
        self._right_anim = False
        self._left_anim = False
        self._on_platform = False
        self.animations = [pygame.image.load('images/stay.png'), pygame.image.load('images/stay2.png'),
                           pygame.image.load('images/sit.png'), pygame.image.load('images/sit2.png'),
                           pygame.image.load('images/shoot.png'),
                           pygame.image.load('images/shoot2.png')]
        self.bullets = []
        self._shoot_f = False
        self._last_shoot = 0

    def move(self):
        if self._move_left_f:
            self._move_left()
        if self._move_right_f:
            self._move_right()

    def move_y(self, platforms):
        self._fall(platforms)

    def _fall(self, platforms):

        self.rect.bottom += self.speed_y
        # for platform in platforms:
        #     platform.rect.centery -= self.speed_y
        self._moment_speed_y += 0.16
        self.speed_y += self._moment_speed_y

        if self._stay_on_platform(platforms):
            self.speed_y = -5
            self._moment_speed_y = -2

    def animation(self, platforms):
        if self._on_platform:
            if self._right_anim:
                self.image = self.animations[2]
            else:
                self.image = self.animations[3]
        elif self._shoot_f:
            if self._right_anim:
                self.image = self.animations[4]
            else:
                self.image = self.animations[5]
        else:
            if self._left_anim:
                self.image = self.animations[1]
            else:
                self.image = self.animations[0]

    def _stay_on_platform(self, platforms):
        for platform in platforms:
            if abs(
                    self.rect.bottom - platform.rect.top) < self.speed_y and platform.rect.right >= self.rect.centerx >= platform.rect.left and self.speed_y >= 0:
                self.rect.bottom = platform.rect.top
                self._on_platform = True
                return True
        self._on_platform = False
        return False

    def shoot(self):
        if self._shoot_f and pygame.time.get_ticks() - self._last_shoot >= 250:
            self._last_shoot = pygame.time.get_ticks()
            blt = Bullet(self.screen, self.setting)
            blt.start_position([self.rect.centerx, self.rect.top])
            blt.speed = blt.speed - self.speed_y / 500
            self.bullets.append(blt)

        print(len(self.bullets))

        for blt in self.bullets:
            blt.move()
            if not blt.is_on_field():
                self.bullets.remove(blt)
            blt.blit()
