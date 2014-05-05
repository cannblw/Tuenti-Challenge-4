import sys

from enum import Enum
import itertools

class Directions (int):
	r = 1
	d = 2
	l = 3
	u = 4


# Set the default direction to right
direction = Directions.r

# Set the initial position
position = [0, 0]

# Initialize the board
board = []

# Init position arrays
dashPositions = []
slashPositions = []
bslashPositions = []
verticalPositions = []
startPositions = []


#########################################

def move ():
	global direction

	if direction == Directions.r:
		position[0] += 1
	elif direction == Directions.l:
		position[0] -= 1
	elif direction == Directions.u:
		position[1] -= 1
	elif direction == Directions.d:
		position[1] += 1

def changeDirection (newDirection):
	global direction
	direction = newDirection
	

def place (character):
	global board

	board[position[1]][position[0]] = character

def computePositions (action):
	global direction

	global dashPositions, slashPositions, bslashPositions, verticalPositions, startPositions

	if action == '#':
		startPositions.append ([position[0],position[1]])
	elif action == '-':
		if direction == Directions.r or direction == Directions.l:
			dashPositions.append ([position[0],position[1]])
		else:
			verticalPositions.append ([position[0],position[1]])
	elif action == '/':
		slashPositions.append ([position[0],position[1]])
		if direction == Directions.r or direction == Directions.l:
			direction = direction - 1
		else:
			direction = direction + 1
	elif action == '\\':
		bslashPositions.append ([position[0],position[1]])

		if direction == Directions.r or direction == Directions.l:
			direction = direction + 1
		else:
			direction = direction - 1

	if direction > 4: direction = direction - 4
	if direction < 1: direction = direction + 4

	move ()


#########################################

def main ():
	# Read stdin
	stdin = sys.stdin.readlines()
	# OR
	#stdin = [line.rstrip() for line in open('stdin.txt')]
	#

	for action in stdin[0]:
		computePositions (action)
		
	# Get board size and offsets
	positionsArray = []
	positionsArray.append (dashPositions)
	positionsArray.append (slashPositions)
	positionsArray.append (bslashPositions)
	positionsArray.append (verticalPositions)
	positionsArray.append (startPositions)

	positionsArray = list(itertools.chain.from_iterable(positionsArray))
	
	xOffset = abs ( min ([x[0] for x in positionsArray]) )
	xMax = max ([x[0] for x in positionsArray]) + xOffset

	yOffset = abs ( min ([x[1] for x in positionsArray]) )
	yMax = max ([x[1] for x in positionsArray]) + yOffset

	# Create the board
	for _ in range (yMax+1):
		board.append ([' ']*(xMax+1))

	# Place the items
	for [y,x] in dashPositions:
		y += xOffset
		x += yOffset
		if x > yMax: x = x - yMax - 1
		if y > xMax: y = y - xMax - 1
		board[x][y] = '-'

	
	for [y,x] in slashPositions:
		y += xOffset
		x += yOffset
		if x > yMax: x = x - yMax - 1
		if y > xMax: y = y - xMax - 1
		board[x][y] = '/'
		
	for [y,x] in bslashPositions:
		y += xOffset
		x += yOffset
		if x > yMax: x = x - yMax - 1
		if y > xMax: y = y - xMax - 1
		board[x][y] = '\\'

	for [y,x] in verticalPositions:
		y += xOffset
		x += yOffset
		if x > yMax: x = x - yMax - 1
		if y > xMax: y = y - xMax - 1
		board[x][y] = '|'

	for [y,x] in startPositions:
		y += xOffset
		x += yOffset
		if x > yMax: x = x - yMax - 1
		if y > xMax: y = y - xMax - 1
		board[x][y] = '#'

	# Draw the board
	for row in board:
		for item in row:
			sys.stdout.write (item)
		sys.stdout.write ("\n")


if __name__ == '__main__':
	main ()