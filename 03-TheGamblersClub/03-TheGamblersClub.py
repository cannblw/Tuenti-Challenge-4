import sys

def main ():
	# Read stdin
	stdin = iter(sys.stdin.readlines())
	stdin.__next__ ()
	# OR
	#stdin = [line.rstrip() for line in open('stdin.txt')] # ERASE FIRST LINE OF FILE
	#
	
	for line in stdin:
		x, y = line.split ()
		x = int(x)
		y = int(y)

		result = round ( (x**2 + y**2) ** 0.5, 2 )

		# Integer check
		if result - int(result) == 0:
			print ( int(result) )
		else:
			print (result)
	

if __name__ == '__main__':
	main ()
	