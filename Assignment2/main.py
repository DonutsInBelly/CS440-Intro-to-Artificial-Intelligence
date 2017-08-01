import random as rn
import draw as draw

board = draw.Board(50,50)
board.init_board()
board.show_board()

x = 0
y = 0

# board.inorderSearch()
# board.baye_1()
#board.baye_2()
# board.rule1()
total_tries = 0
total_steps = 0


for i in range(100):
	(cur_tires, cur_steps) = board.num_4()
	total_tries += cur_tires
	total_steps += cur_steps
	board.changeGoal()
	board.show_board()

avg_t = total_tries / float(100)
avg_s = total_steps / float(100)
print("Final Try Average = " + str(avg_t) + ", Final Step Average:" + str(avg_s))

#while True:
 #	board.show_board()
