import sys
import random
import pygame as pygame
import numpy as np

cell_size = 15

# Terrain
white =         (255, 255, 255)
light_gray =    (204, 204, 204)  # Flatland
green =         (0, 153, 51)  # Hilly
dark_green =    (0, 51, 0)  # Forested
gray =          (153, 153, 153)  # Caves
light_green =   (153, 255, 153)  # Start
red =           (255, 0, 0)  # Goal
black =         (0, 0, 0)
blue =          (0, 0, 200)

class Board(object):
    """docstring for Board."""
    def __init__(self, width, height):
        super(Board, self).__init__()
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.tries = 0
        self.cells = {} # A dictionary of tuples, for each will be a list of values

        # Defines each cell in self.cells
        for x in range(width):
            for y in range(height):
                self.cells[(x, y)] = {'state': None,     # None, Flat, Hilly, Forest, or Caves
                                     'prob': None,      # Probability
                                     'is_goal': False,  # Weather or not it is the goal node
                                     'chance_of_goal': None}    # Keep track of path

        # Sets probabilities for each cell in the board
        for x in range(width):
            for y in range(height):
                p = random.random()
                if p <= 0.25:
                    self.cells[(x, y)]['state'] = 'Flat'
                    self.cells[(x, y)]['prob'] = np.float64(0.2)
                elif p <= 0.5:
                    self.cells[(x, y)]['state'] = 'Hilly'
                    self.cells[(x, y)]['prob'] = np.float64(0.4)
                elif p <= 0.75:
                    self.cells[(x, y)]['state'] = 'Forest'
                    self.cells[(x, y)]['prob'] = np.float64(0.6)
                elif p <= 1.0:
                    self.cells[(x, y)]['state'] = 'Caves'
                    self.cells[(x, y)]['prob'] = np.float64(0.9)

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
                top = (x * cell_size) + 1
                left = (y * cell_size) + 1
                r = pygame.Rect(left, top, cell_size - 1, cell_size - 1)
                if self.cells[(x, y)]['is_goal']:
                    pygame.draw.rect(self.background, red, r, 0)
                elif self.cells[(x, y)]['state'] == 'Flat':
                    pygame.draw.rect(self.background, light_gray, r, 0)
                elif self.cells[(x, y)]['state'] == 'Hilly':
                    pygame.draw.rect(self.background, light_green, r, 0)
                elif self.cells[(x, y)]['state'] == 'Forest':
                    pygame.draw.rect(self.background, dark_green, r, 0)
                elif self.cells[(x, y)]['state'] == 'Caves':
                    pygame.draw.rect(self.background, gray, r, 0)

    # Refresh function
    def show_board(self):
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()
        running = True
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
        except SystemExit:
            pygame.quit()

    def changeGoal(self):
        self.cells[(self.n, self.m)]['is_goal'] = False
        self.n = int(self.width * random.random())
        self.m = int(self.height * random.random())
        self.cells[(self.n, self.m)]['is_goal'] = True

    # Creates probability matrix w/ initial values
    def init_prob(self):
        self.prob_max = 1.0/(self.width*self.height)
        self.prob_prev = 0.0
        self.prob = [[0 for x in range(self.width)] for y in range(self.height)]
        for x in range(self.width):
            for y in range(self.height):
                self.prob[x][y] = 1.0/(self.width*self.height)

    def rule1(self):
        belief = {}
        # Initialize belief states
        for x in range(self.width):
            for y in range(self.height):
                belief[(x,y)] = float(1)/(self.width * self.height)
                # belief[(x, y)] = random.random()
        # Start Search
        tries = 0
        found_goal = False
        curx = 0
        cury = 0
        while found_goal == False:
            # Search cell
            tries += 1
            roll = random.random()
            checkedBt = belief[(x, y)]
            checkedProb = self.cells[(curx, cury)]['prob']
            print("Try: " + str(tries) + ", Checking " + str(curx) + ", " + str(cury) + " with probability: " + str(belief[curx,cury]) + "; Goal at: (" + str(self.n) + ", " + str(self.m) + ")")
            # print(tries)
            if roll <= checkedProb:
                if self.cells[(curx, cury)]['is_goal']:
                    found_goal = True
                    break
            # Update belief states and pick new curx and cury
            newx = 0
            newy = 0
            curBt = belief[(0,0)]
            if self.cells[(0,0)]['is_goal']:
                belief[(0,0)] = np.float64(checkedBt * checkedProb)/((checkedBt * checkedProb) + (1 - checkedBt))
                # belief[(0,0)] = np.float64(checkedBt * checkedProb)/((belief[(0,0)] * self.cells[(0,0)]['prob']) + (1 - checkedBt))
            else:
                belief[(0,0)] = np.float64(curBt)/((checkedBt * checkedProb) + (1 - checkedBt))
                # belief[(0,0)] = np.float64(curBt)/((belief[(0,0)] * self.cells[(0,0)]['prob']) + (1 - checkedBt))
            for x in range(self.width):
                for y in range(self.height):
                    curBt = belief[(x,y)]
                    curProb = self.cells[(x,y)]['prob']
                    if x == curx and y == cury:
                        # if x == self.n and y == self.m:
                        #     belief[(x,y)] = np.float64((checkedBt * checkedProb))/((checkedBt * checkedProb) + (1 - checkedBt))
                        # else:
                        #     # belief[(x,y)] = np.float64(curBt)/((checkedBt * checkedProb) + (1 - checkedBt))
                        belief[(x,y)] = np.float64((checkedBt * checkedProb))/((checkedBt * checkedProb) + (1 - checkedBt))
                        # belief[(x,y)] = np.float64(checkedBt * checkedProb)/((belief[(x,y)] * self.cells[(x,y)]['prob']) + (1 - checkedBt))
                    else:
                        belief[(x,y)] = np.float64(curBt)/((checkedBt * checkedProb) + (1 - checkedBt))
                        # belief[(x,y)] = np.float64(curBt)/((belief[(x,y)] * self.cells[(x,y)]['prob']) + (1 - checkedBt))
                    # print("New Belief of (" + str(x) + ", " + str(y) + "): " + str(belief[(x,y)]))
            for x in range(self.width):
                for y in range(self.height):
                    if belief[(newx, newy)] < belief[(x,y)]:
                        # print("New x and y")
                        newx = x
                        newy = y
            # print(belief)
            curx = newx
            cury = newy
        print("Finished with : " + str(tries))
        return tries

    def rule2(self):
        belief = {}
        # Initialize belief states
        for x in range(self.width):
            for y in range(self.height):
                belief[(x,y)] = (float(1)/(self.width * self.height)) #* (1 - self.cells[(x,y)]['prob'])
                # belief[(x, y)] = random.random()
        # Start Search
        tries = 0
        found_goal = False
        curx = 0
        cury = 0
        while found_goal == False:
            # Search cell
            tries += 1
            roll = random.random()
            checkedBt = belief[(x, y)]
            checkedProb = self.cells[(curx, cury)]['prob']
            print("Try: " + str(tries) + ", Checking " + str(curx) + ", " + str(cury) + " with probability: " + str(belief[curx,cury]) + "; Goal at: (" + str(self.n) + ", " + str(self.m) + ")")
            # print(tries)
            if roll <= checkedProb:
                if self.cells[(curx, cury)]['is_goal']:
                    found_goal = True
                    break
            # Update belief states and pick new curx and cury
            newx = 0
            newy = 0
            # curBt = belief[(0,0)]
            # belief[(0,0)] = np.float64(1 - self.cells[(x,y)]['prob']) * curBt
            belief[(curx,cury)] = np.float64(1 - self.cells[(curx,cury)]['prob']) * (belief[(curx,cury)])
            # for x in range(self.width):
            #     for y in range(self.height):

            for x in range(self.width):
                for y in range(self.height):
                    if belief[(newx, newy)] < belief[(x,y)]:
                        # print("New x and y")
                        newx = x
                        newy = y
            # print(belief)
            curx = newx
            cury = newy
        print("Finished with : " + str(tries))
        return tries

    def inorderSearch(self):
        self.tries = 0
        found_goal = False
        while found_goal == False:
            for x in range(self.width):
                for y in range(self.height):
                    # print(self.tries)
                    self.tries += 1
                    roll = random.random()
                    if roll <= self.cells[(x, y)]['prob']:
                        if self.cells[(x, y)]['is_goal'] == True:
                            print('ayy')
                            found_goal = True
                            break
        print(self.tries)

    def update_current(self, i, j):
        for x in range(self.width):
            for y in range(self.height):
                top = (x * cell_size) + 1
                left = (y * cell_size) + 1
                r = pygame.Rect(left, top, cell_size - 1, cell_size - 1)
                if self.cells[(x, y)]['is_goal']:
                    pygame.draw.rect(self.background, red, r, 0)
                elif self.cells[(x, y)]['state'] == 'Flat':
                    pygame.draw.rect(self.background, light_gray, r, 0)
                elif self.cells[(x, y)]['state'] == 'Hilly':
                    pygame.draw.rect(self.background, light_green, r, 0)
                elif self.cells[(x, y)]['state'] == 'Forest':
                    pygame.draw.rect(self.background, dark_green, r, 0)
                elif self.cells[(x, y)]['state'] == 'Caves':
                    pygame.draw.rect(self.background, gray, r, 0)
        top = (i * cell_size) + 1
        left = (j * cell_size) + 1
        r = pygame.Rect(left, top, cell_size - 1, cell_size - 1)
        pygame.draw.rect(self.background, blue, r, 0)


    def normalize(self, x, y):
        scalar = (1.0-self.prob[x][y])/(1.0-self.prob_prev)
        self.prob_max = 0.0
        for i in range(self.width):
            for j in range(self.height):
                self.prob[i][j] = scalar*self.prob[i][j]
                if(self.prob[i][j] > self.prob_max):
                    self.prob_max = self.prob[i][j]
                    self.x = i
                    self.y = j
                #self.show_board()


    def baye_1(self):
        self.tries = 0
        self.init_prob()
        x = int (random.random() * self.width)
        y = int (random.random() * self.height)
        found_goal = False
        while found_goal == False:
            # self.update_current(x, y)
            self.show_board()
            self.tries += 1
            roll = random.random()
            if (roll <= self.cells[(x, y)]['prob']) and (self.cells[(x, y)]['is_goal'] == True):
                print('ayy')
                print(self.cells[(x, y)]['state'] +": " + str(self.cells[(x, y)]['prob']))
                found_goal = True
                break
            else:
                self.prob_prev = self.prob[x][y]
                self.prob[x][y] = self.prob[x][y]*((1-self.cells[(x, y)]['prob'])/(1-self.prob[x][y]))  # Bayes' Theorem
                # self.prob[x][y] = self.prob[x][y]*(1-self.cells[(x, y)]['prob'])/((self.prob[x][y]*(1-self.cells[(x, y)]['prob']))+(1-self.prob[x][y])) # Bayes' Theorem, with the denom expanded
                # UNCOMMENT ABOVE IF YOU WANT TO BE A LITTLE MORE CORRECT... (TIME CONSUMING)
                self.normalize(x, y)
                x = self.x
                y = self.y
                # print(str(self.tries) + ": " + str(self.prob_max))
        print(self.tries)

    def baye_2(self):
        self.tries = 0
        self.init_prob()
        x = int (random.random() * self.width)
        y = int (random.random() * self.height)
        found_goal = False
        while found_goal == False:
            # self.update_current(x, y)
            self.show_board()
            self.tries += 1
            roll = random.random()
            if (roll <= self.cells[(x, y)]['prob']) and (self.cells[(x, y)]['is_goal'] == True):
                print('ayy')
                print(self.cells[(x, y)]['state'] +": " + str(self.cells[(x, y)]['prob']))
                found_goal = True
                break
            else:
                self.prob_prev = self.prob[x][y]
                self.prob[x][y] = self.prob[x][y]*((1-self.cells[(x, y)]['prob'])/(1-self.prob[x][y]))  # Bayes' Theorem
                # self.prob[x][y] = self.prob[x][y]*(1-self.cells[(x, y)]['prob'])/((self.prob[x][y]*(1-self.cells[(x, y)]['prob']))+(1-self.prob[x][y])) # Bayes' Theorem, with the denom expanded
                # UNCOMMENT ABOVE IF YOU WANT TO BE A LITTLE MORE CORRECT... (TIME CONSUMING)
                self.prob[x][y] = self.prob[x][y] * self.cells[(x, y)]['prob']  # Here, we scale the probability by the cell's likelihood of finding the goal, thereby prioritizing environments where finding the target is more likely
                self.normalize(x, y)
                x = self.x
                y = self.y
                # print(str(self.tries) + ": " + str(self.prob_max))
        print(self.tries)
