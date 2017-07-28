import random as rn
import draw as draw

board = draw.Board(50,50)
board.init_board()
board.show_board()

x = 0
y = 0

board.inorderSearch()
board.baye_1()
board.baye_2()

while True:
	board.show_board()