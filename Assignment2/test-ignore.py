import sys
import random
import pygame

cell_size = 100
num_cells = 5
# num_x_cells = 0
# num_y_cells= 0

# Terrain
white =         (255, 255, 255)
light_gray =    (179, 255, 179) #(204, 204, 204)  # Flatland
green =         (102, 255, 102)#(0, 153, 51)  # Hilly
dark_green =    (26, 255, 26)#(0, 51, 0)  # Forested
gray =          (0, 204, 0)#(153, 153, 153)  # Caves
light_green =   (153, 255, 153)  # Start
red =           (255, 0, 0)  # Goal
black =         (0, 0, 0)

# More variables and what not
# start_placed = False
# goal_placed = False
# start = None
# goal = None

cells = {}  # A dictionary of tuples, for each will be a list of values

for x in range(num_cells):
    for y in range(num_cells):
        cells[(x, y)] = {'state': None,     # None, Flat, Hilly, Forest, or Caves
                         'prob': None,      # Probability
                         'is_goal': False,  # Weather or not it is the goal node
                         'parent': None}    # Keep track of path

for x in range(num_cells):
    for y in range(num_cells):
        p = random.random()
        if p <= 0.25:
            cells[(x, y)]['state'] = 'Flat'
            cells[(x, y)]['prob'] = 0.8
        elif p <= 0.5:
            cells[(x, y)]['state'] = 'Hilly'
            cells[(x, y)]['prob'] = 0.6
        elif p <= 0.75:
            cells[(x, y)]['state'] = 'Forest'
            cells[(x, y)]['prob'] = 0.4
        elif p <= 1.0:
            cells[(x, y)]['state'] = 'Caves'
            cells[(x, y)]['prob'] = 0.1

# PyGame stuff you gotta do
pygame.init()
size = width, height = (cell_size * num_cells) + 2, (cell_size * num_cells) + 2
screen = pygame.display.set_mode(size)
pygame.display.set_caption = 'Grid'

# Draw's initial board
def init_board(board):
    background = pygame.Surface(board.get_size())
    background = background.convert()
    background.fill(light_gray)

    for i in range(0, (cell_size * num_cells) + 1)[::cell_size]:
        pygame.draw.line(background, white, (i, 0), (i, cell_size * num_cells), 2)
        pygame.draw.line(background, white, (0, i), (cell_size * num_cells, i), 2)
    return background

# Refresh function
def show_board(screen, board):
    screen.blit(board, (0, 0))
    pygame.display.flip()

# Makes board real
board = init_board(screen)

while True:
    show_board(screen, board)
