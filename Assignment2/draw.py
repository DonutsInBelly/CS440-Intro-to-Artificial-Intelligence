import sys
import random
import pygame as pygame

cell_size = 100

# Terrain
white =         (255, 255, 255)
light_gray =    (179, 255, 179) #(204, 204, 204)  # Flatland
green =         (102, 255, 102)#(0, 153, 51)  # Hilly
dark_green =    (26, 255, 26)#(0, 51, 0)  # Forested
gray =          (0, 204, 0)#(153, 153, 153)  # Caves
light_green =   (153, 255, 153)  # Start
red =           (255, 0, 0)  # Goal
black =         (0, 0, 0)

class Board(object):
    """docstring for Board."""
    def __init__(self, width, height):
        super(Board, self).__init__()
        self.width = width
        self.height = height
        self.cells = {} # A dictionary of tuples, for each will be a list of values
        # Defines each cell in self.cells
        for x in range(width):
            for y in range(height):
                self.cells[(x, y)] = {'state': None,     # None, Flat, Hilly, Forest, or Caves
                                     'prob': None,      # Probability
                                     'is_goal': False,  # Weather or not it is the goal node
                                     'parent': None}    # Keep track of path
        # Sets probabilities for each cell in the board
        for x in range(width):
            for y in range(height):
                p = random.random()
                if p <= 0.25:
                    self.cells[(x, y)]['state'] = 'Flat'
                    self.cells[(x, y)]['prob'] = 0.8
                elif p <= 0.5:
                    self.cells[(x, y)]['state'] = 'Hilly'
                    self.cells[(x, y)]['prob'] = 0.6
                elif p <= 0.75:
                    self.cells[(x, y)]['state'] = 'Forest'
                    self.cells[(x, y)]['prob'] = 0.4
                elif p <= 1.0:
                    self.cells[(x, y)]['state'] = 'Caves'
                    self.cells[(x, y)]['prob'] = 0.1
        # Picks a random (n,m) to be the Goal
        self.n = int(width * random.random())
        self.m = int(height * random.random())
        for x in range(width):
            for y in range(height):
                if x == self.n and y == self.m:
                    self.cells[(x, y)]['is_goal'] = True
        # Pygame setup
        pygame.init()
        self.size = width, height = (cell_size * width) + 2, (cell_size * height) + 2
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption = 'Grid'

    # Draw's initial board
    def init_board(self):
        background = pygame.Surface(self.screen.get_size())
        background = background.convert()
        background.fill(light_gray)

        for i in range(0, (cell_size * self.width) + 1)[::cell_size]:
            pygame.draw.line(background, white, (i, 0), (i, cell_size * self.width), 2)
            pygame.draw.line(background, white, (0, i), (cell_size * self.height, i), 2)
        self.background = background
        # Assigns color to cell depending on terrain type given
        for x in range(self.width):
            for y in range(self.height):
                top = (x * cell_size) + 2
                left = (y * cell_size) + 2
                if self.cells[(x, y)]['state'] == 'Flat':
                    r = pygame.Rect(left, top, cell_size - 2, cell_size - 2)
                    pygame.draw.rect(self.background, light_gray, r, 0)
                elif self.cells[(x, y)]['state'] == 'Hilly':
                    r = pygame.Rect(left, top, cell_size - 2, cell_size - 2)
                    pygame.draw.rect(self.background, light_green, r, 0)
                elif self.cells[(x, y)]['state'] == 'Forest':
                    r = pygame.Rect(left, top, cell_size - 2, cell_size - 2)
                    pygame.draw.rect(self.background, dark_green, r, 0)
                elif self.cells[(x, y)]['state'] == 'Caves':
                    r = pygame.Rect(left, top, cell_size - 2, cell_size - 2)
                    pygame.draw.rect(self.background, gray, r, 0)


    # Refresh function
    def show_board(self):
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()
