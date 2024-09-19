# Copy of John Conway's Game of Life

# Any live cell with fewer than two live neighbours dies, as if by underpopulation

# Any live cell with two or three live neighbours lives on to the next generation.

# Any live cell with more than three live neighbours dies, as if by overpopulation.

# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

import time
import pygame
import numpy as np
from pygame import mixer

COLOR_BG = (0, 179, 255)
COLOR_GRID = (3, 101, 143)
COLOR_DIE_NEXT = (50, 166, 40)
COLOR_ALIVE_NEXT = (52, 209, 38)

pygame.init()

pygame.display.set_caption('  Game of Life')

def update(screen, cells, size, with_progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        color = COLOR_BG if cells[row, col] == 0 else COLOR_ALIVE_NEXT

        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if with_progress:
                    color = COLOR_DIE_NEXT
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT
        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT

        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

    return updated_cells


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

    cells = np.zeros((70, 130))
    screen.fill(COLOR_GRID)
    update(screen, cells, 15)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for Q in pygame.event.get():
            if Q.type == pygame.QUIT:
                pygame.quit()
                return
            elif Q.type == pygame.KEYDOWN:
                if Q.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, 15)
                    pygame.display.update()
                    
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = pos[1] // 15, pos[0] // 15
                if cells[row, col] == 1:
                    cells[row, col] = 0
                else:
                    cells[row, col] = 1
                update(screen, cells, 15)
                pygame.display.update()

        screen.fill(COLOR_GRID)

        if running:
            cells = update(screen, cells, 15, with_progress=True)
            pygame.display.update()

        time.sleep(0.001)



if __name__ == "__main__":
    main()
