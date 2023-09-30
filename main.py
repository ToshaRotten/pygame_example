import sys
import pygame

from player import player
from animation import animation
from window import window
from levels import level
from menu import menu

pygame.init()

window = window.Window(640, 640)

player_anim = animation.Animation("animation/anim/")
player = player.Player(32, 32, player_anim, 100)

window = pygame.display.set_mode((window.height, window.width))
window.fill((255, 255, 255))

level = level.Level("levels/level1.csv")

selector = 1

while True:
    menu.menu(selector)
    # level.Draw(window)
    # player.Draw(window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            selector += menu.menu_update(event)
            player.Move(event)