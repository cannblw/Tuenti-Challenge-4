import sys

inTree = []
iterCount = 0

def connectedTo (id, endingId, phones):
	global iterCount

	inTree.append (id)
	sons = []

	phones.seek (0)

	for line in phones:
		line = line.strip().split (' ')

		if (line[0] == id):
			sons.append (line[1])
		elif (line[1] == id):
			sons.append (line[0])

	if endingId in sons:
		print ('Connected at', iterCount),
		exit ()

	iterCount += 1

	# Call function for each son
	for t in sons:
		if t not in inTree:
			connectedTo (t, endingId, phones)


def main ():
	# Read stdin
	stdin = iter(sys.stdin.readlines())
	# OR
	stdin = [line.rstrip() for line in open('stdin.txt')]
	#

	phones = open ('phone_call.log', 'r')

	connectedTo (stdin[0], stdin[1], phones)

	sys.stdout.write ('Not connected')

if __name__ == '__main__':
	main ()
