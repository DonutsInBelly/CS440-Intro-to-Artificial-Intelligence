import random as rn
import draw as draw

board = draw.Board(50,50)
board.init_board()

board.inorderSearch()
x = 0
y = 0
while True:
    board.tries += 1
    if x > board.width:
        x = 0
        y = 0
    roll = rn.random()
    if roll <= board.cells[(x, y)]['prob']:
        if board.cells[(x, y)]['is_goal']:
            break
    board.show_board()
