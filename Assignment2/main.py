import random as rn
import draw as draw

board = draw.Board(50,50)
board.init_board()
board.show_board()

x = 0
y = 0

# board.inorderSearch()
# board.baye_1()
# board.baye_2()
# board.rule1()
total = 0
for i in range(15):
	cur = board.rule1()
	total += cur
	board = draw.Board(50,50)

avg = total / float(15)
print("Final Average = " + str(avg))
# while True:
# 	board.show_board()
