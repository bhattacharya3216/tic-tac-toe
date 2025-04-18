from random import randrange


def display(board):
	print("+-------" * 3,"+", sep="")
	for row in range(3):
		print("|       " * 3,"|", sep="")
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")


def user_input(board):
	var = False
	while not var:
		user = input("Enter your move: ")
		var = len(user) == 1 and user >= '1' and user <= '9'
		if not var:
			print("Bad move - repeat your input!")
			continue
		user = int(user) - 1
		row = user // 3
		col = user % 3
		sgn = board[row][col]
		var = sgn not in ['O','X']
		if not var:
			print("Field already occupied - repeat your input!")
			continue
	board[row][col] = 'O'


def free_blocks(board):
	remaining_blocks = []
	for row in range(3):
		for col in range(3):
			if board[row][col] not in ['O','X']:
				remaining_blocks.append((row,col))
	return remaining_blocks


def victory(board,sign):
	if sign == "X":
		who = 'comp'
	elif sign == "O":
		who = 'user'
	else:
		who = None
	d1 = d2 = True
	for rc in range(3):
		if board[rc][0] == sign and board[rc][1] == sign and board[rc][2] == sign:
			return who
		if board[0][rc] == sign and board[1][rc] == sign and board[2][rc] == sign:
			return who
		if board[rc][rc] != sign:
			d1 = False
		if board[2 - rc][2 - rc] != sign:
			d2 = False
	if d1 or d2:
		return who
	return None


def comp_input(board):
	free = free_blocks(board)
	limit = len(remaining_blocks)
	if limit > 0:
		p = randrange(limit)
		row, col = remaining_blocks[p]
		board[row][col] = 'X'


board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ]
board[1][1] = 'X'
remaining_blocks = free_blocks(board)
turn = True
while len(remaining_blocks):
	display(board)
	if turn:
		user_input(board)
		winner = victory(board,'O')
	else:
		comp_input(board)
		winner = victory(board,'X')
	if winner != None:
		break
	turn = not turn
	remaining_blocks = free_blocks(board)

display(board)
if winner == 'user':
	print("You won!")
elif winner == 'comp':
	print("I won")
else:
	print("Tie!")
