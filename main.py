import sys
import pygame
import math
from player import player
from animation import animation
from window import window
from levels import level
from menu import menu

pygame.init()

BLACK = (0,0,0)

window = window.Window(640, 640)



player_anim = animation.Animation("animation/anim/")
player = player.Player(32, 32, player_anim, 100)

window = pygame.display.set_mode((window.height, window.width))
window.fill((255, 255, 255))

level = level.Level("levels/level1.csv")

selector = 1


bullet = [0, 0]
bullet[0] = player.x
bullet[1] = player.y
angle = 0
bullet_visible = True
is_move = False

while True:
    # level.Draw(window)
    # player.Draw(window)

    pygame.draw.circle(window, (255,255,255), (0, 0), 10)

    if is_move:
        bullet[0] = bullet[0] + math.cos(angle) * 5
        bullet[1] = bullet[1] + math.sin(angle) * 5


    print(bullet)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # selector += menu.menu_update(event)
            player.Move(event)
        if event.type == pygame.MOUSEBUTTONDOWN:

            is_move = True
            bullet_visible = True
            mouse_pos = pygame.mouse.get_pos()
            dx = mouse_pos[0] - bullet[0]
            dy = mouse_pos[1] - bullet[1]
            angle = math.atan2(dy, dx)
