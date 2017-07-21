import sys
import random
import pygame

cell_size = 20
num_cells = 20
# num_x_cells = 0
# num_y_cells= 0

# Terrain
white = (255, 255, 255)
light_gray = (204, 204, 204)  # Flatland
green = (0, 153, 51)  # Hilly
dark_green = (0, 51, 0)  # Forested
gray = (153, 153, 153)  # Caves
light_green = (153, 255, 153)  # Start
red = (255, 77, 77)  # Goal

# More variables and what not
# start_placed = False
# goal_placed = False
# start = None
# goal = None

cells = {}  # A dictionary of tuples, for each will be a list of values

for x in range(num_cells):
    for y in range(num_cells):
        cells[(x, y)] = {'state': None,  # None, Flat, Hilly, Forest, or Caves
                         'parent': None}  # Keep track of path

for x in range(num_cells):
    for y in range(num_cells):
        p = random.random()
        if p <= 0.25:
            cells[(x, y)] = {'state': 'Flat'}
        elif p <= 0.5:
            cells[(x, y)] = {'state': 'Hilly'}
        elif p <= 0.75:
            cells[(x, y)] = {'state': 'Forest'}
        elif p <= 1.0:
            cells[(x, y)] = {'state': 'Caves'}

# PyGame stuff you gotta do
pygame.init()
size = width, height = (cell_size * num_cells) + 2, (cell_size * num_cells) + 2
screen = pygame.display.set_mode(size)
pygame.display.set_caption = 'Grid'


# Refresh function
def show_board(screen, board):
    screen.blit(board, (0, 0))
    pygame.display.flip()


# Draw's initial board
def init_board(board):
    background = pygame.Surface(board.get_size())
    background = background.convert()
    background.fill(light_gray)

    for i in range(0, (cell_size * num_cells) + 1)[::cell_size]:
        pygame.draw.line(background, white, (i, 0), (i, cell_size * num_cells), 1)
        pygame.draw.line(background, white, (0, i), (cell_size * num_cells, i), 1)
    return background


# returns Boolean value for if a certain node is on the board
def on_board(node):
    x, y = node
    return x >= 0 and x < num_cells and y >= 0 and y <= num_cells


# Functions for movement, will be used later
# This defines the orthogonal children
def orthogonals(current):
    x, y = current

    n = x - 1, y
    s = x + 1, y
    e = x, y + 1
    w = x, y - 1

    directions = [n, e, s, w]
    return [x for x in directions if on_board(x)]


# This will give each child the 'parent' that the program stepped from
def update_child(parent, child):  # Here is where you would might add 'cost to value'
    cells[child]['parent'] = parent


# Makes board real
board = init_board(screen)

# Out of place and weird loop for assigning each space it's color
for x in range(num_cells):
    for y in range(num_cells):
        top = (x * cell_size) + 1
        left = (y * cell_size) + 1
        if cells[(x, y)]['state'] == 'Flat':
            r = pygame.Rect(left, top, cell_size - 1, cell_size - 1)
            pygame.draw.rect(board, light_gray, r, 0)
        elif cells[(x, y)]['state'] == 'Hilly':
            r = pygame.Rect(left, top, cell_size - 1, cell_size - 1)
            pygame.draw.rect(board, light_green, r, 0)
        elif cells[(x, y)]['state'] == 'Forest':
            r = pygame.Rect(left, top, cell_size - 1, cell_size - 1)
            pygame.draw.rect(board, dark_green, r, 0)
        elif cells[(x, y)]['state'] == 'Caves':
            r = pygame.Rect(left, top, cell_size - 1, cell_size - 1)
            pygame.draw.rect(board, gray, r, 0)

# Main loop, this is where the magic happens (in theory)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        key = pygame.key.get_pressed()
        left_click, middle_click, right_click = pygame.mouse.get_pressed()

        # Key events
        enter = key[pygame.K_RETURN]
        backspace = key[pygame.K_BACKSPACE]

        # See where you clicked
        x, y = pygame.mouse.get_pos()
        # Get top-left-corner of cell
        top = ((x / cell_size) * cell_size) + 2
        left = ((y / cell_size) * cell_size) + 2
        # Get the index of the cell, ya know, not the pixelly version
        x_index = (left - 2) / cell_size
        y_index = (top - 2) / cell_size

        show_board(screen, board)
