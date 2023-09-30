import pygame
def menu(selector):
    print(selector)
    if selector == 1:
        print("game")
    elif selector == 2:
        print("settings")
    elif selector == 3:
        print("exit")

def menu_update(event):
    if event.key == pygame.K_UP:
        return -1
    elif event.key == pygame.K_DOWN:
        return 1