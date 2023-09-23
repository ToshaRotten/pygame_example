import pygame
class Player:
    def __init__(self, x, y, animation, HP):
        self.x = x
        self.y = y
        self.animation = animation
        self.HP = HP


    def Draw(self, window):
        self.animation.draw(window, self.x, self.y)


    def Move(self, event):
        if event.key == pygame.K_UP:
            self.y -= 32
        elif event.key == pygame.K_DOWN:
            self.y += 32
        elif event.key == pygame.K_LEFT:
            self.x -= 32
        elif event.key == pygame.K_RIGHT:
            self.x += 32
