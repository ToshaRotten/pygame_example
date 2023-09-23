import pygame

tiles = {
    0:
        pygame.image.load("../img/bricks.png"),
}
class Level:

    def __init__(self, path):
        self.tile_size = 32
        self.path = path
        self.arr = []

        with open(path) as file:
            self.arr = [list(map(int, line.strip().split(","))) for line in file]

        self.height = len(self.arr)
        self.width = len(self.arr[0])


    def Draw(self, window):
        for i in range(self.height):
            for j in range(self.width):
                if self.arr[i][j] == 0:
                    pygame.draw.rect(window, (255,255,255), pygame.Rect(j*32, i*32, 32,32))
                if self.arr[i][j] == 1:
                    window.blit(tiles[0], (j * self.tile_size, i * self.tile_size))

        pygame.display.flip()