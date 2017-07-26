import random as rn
import draw as draw

board = draw.Board(50,50)
board.init_board()

board.inorderSearch()
x = 0
y = 0
while True:
    board.show_board()
