import sys
import pygame

with open("levels/level1.csv") as file:
    map = [list(map(int, line.strip().split(","))) for line in file]

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
BG_COLOR = (255, 255, 255)
BLACK = (0, 0, 0)
player_pos = (1, 1)

pygame.init()

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
window.fill(BG_COLOR)

tiles = {
    0:
        pygame.image.load("img/bricks.png"),
    1:
        pygame.image.load("img/player.jpg")
}

tile_size = 32


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            map[player_pos[1]][player_pos[0]] = 0
            if event.key == pygame.K_UP:
                if map[player_pos[0]][player_pos[1] - 1] != 1:
                    player_pos = (player_pos[0], player_pos[1] - 1)
            elif event.key == pygame.K_DOWN:
                if map[player_pos[0]][player_pos[1] + 1] != 1:
                    player_pos = (player_pos[0], player_pos[1] + 1)
            elif event.key == pygame.K_LEFT:
                if map[player_pos[0] - 1][player_pos[1]] != 1:
                    player_pos = (player_pos[0] - 1, player_pos[1])
            elif event.key == pygame.K_RIGHT:
                if map[player_pos[0] + 1][player_pos[1]] != 1:
                    player_pos = (player_pos[0] + 1, player_pos[1])

        map[player_pos[1]][player_pos[0]] = 2

        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == 0:
                    pygame.draw.rect(window, (255,255,255), pygame.Rect(j*32, i*32, 32,32))
                if map[i][j] == 1:
                    window.blit(tiles[0], (j * tile_size, i * tile_size))
                if map[i][j] == 2:
                    window.blit(tiles[1], (j * tile_size, i * tile_size))

        pygame.display.flip()