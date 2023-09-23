import os
import time
import pygame
class Animation:
    def __init__(self, path):
        self.frames = []
        files_names = os.listdir(path)
        files = []
        for file in files_names:
            self.frames.append(pygame.image.load(path + file))

    def draw(self, window, x, y):

        for f in self.frames:
            pygame.draw.rect(window, (255, 255, 255), pygame.Rect(x, y, 32, 32))
            window.blit(f, (x, y))
            pygame.display.flip()
            time.sleep(0.1)
