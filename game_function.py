import pygame
import sys


def doodle_move(hero, event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_d:
            hero._move_right_f = True
            hero._left_anim = False
            hero._right_anim = True

        if event.key == pygame.K_a:
            hero._move_left_f = True
            hero._left_anim = True
            hero._right_anim = False

        if event.key == pygame.K_SPACE:
            hero._shoot_f = True

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_d:
            hero._move_right_f = False
        if event.key == pygame.K_a:
            hero._move_left_f = False
        if event.key == pygame.K_SPACE:
            hero._shoot_f = False


def check_events(hero):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        doodle_move(hero, event)
