def all_visited(board):
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == -1:
				return False
	return True


def print_knights_tour(board, move, posr, posc):
	board[posr][posc] = move
	if move == len(board[0]) * len(board):
		for lis in board:
			print(lis)
		print("**********")
	# Make next move, choosing from the 8 moves
	possible_moves = [
			(-2, 1),
			(-1, 2),
			(1, 2),
			(2, 1),
			(2, -1),
			(1, -2),
			(-1, -2),
			(-2, -1)
			]
	for x, y in possible_moves:
		if (posr + x)<0 or (posr + x)>=len(board) or (posc + y)<0 or (posc + y)>=len(board[0]) or board[posr + x][posc + y] != -1:
			continue
		else:
			print_knights_tour(board, move+1, posr + x, posc + y)
	board[posr][posc] = -1



if __name__ == '__main__':
	N = 5
	board = [[-1] * N for k in range(0, N)]
	# visited = [[False] * N for k in range(0, N)]
	sti = 2
	stj = 0
	print_knights_tour(board, 1, sti, stj)