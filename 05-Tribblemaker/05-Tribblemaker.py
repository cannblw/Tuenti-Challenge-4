import sys
import copy

def countNeighbours (board, x, y):
	counter = 0

	for i in range (y-1, y+2):
		if i < 0 or i >= 8: continue
		for j in range (x-1, x+2):
			if j < 0 or j >= 8: continue
			if not ((i==y) and (j==x)):
				if board[i][j] == 'X':
					counter += 1
	return counter

def step (board):
	spawn = []
	despawn = []

	board = copy.deepcopy (board)

	for i in range (8):
		for j in range (8):
			neighbours = countNeighbours (board, j, i)

			if board[i][j] == 'X':
				if not neighbours == 2 and not neighbours == 3:
					despawn.append ([i,j])
					
			else:
				if neighbours == 3:
					spawn.append ([i,j])

	for p in spawn:
		board [p[0]][p[1]] = 'X'

	for p in despawn:
		board [p[0]][p[1]] = '-'

	return board

def main ():
	# Read stdin
	stdin = iter(sys.stdin.readlines())
	# OR
	#stdin = [line.rstrip() for line in open('stdin.txt')]
	#

	# All generations array
	# ...or how to full the RAM
	gen = []

	# Create the board
	board = []
	for line in stdin:
		row = [c for c in line]
		board.append (row)

	# Append generation 0
	gen.append (board)

	# Calculate 100 generations
	for i in range (100):
		gen.append (step(gen[i]))

	## Find a pattern from the end

	# Unsorted pattern array
	uPattern = []

	# First element of pattern
	a = gen[-1]

	uPattern.append (a)

	for t in gen[-2::-1]:
		if t == a:
			break

		uPattern.append (t)

	patternSize = len (uPattern)

	# Reverse pattern
	uPattern = uPattern[::-1]

	# Find the pattern from the beginning
	br = False
	for startPosition in range(100):
		for j in range(len(uPattern)):
			if gen[startPosition] == uPattern[j]:
				br = True
				break
		if (br): break


	print (startPosition, patternSize)


if __name__ == '__main__':
	main ()