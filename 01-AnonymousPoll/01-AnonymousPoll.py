import sys
import gzip

def main ():
	# Read file
	f = gzip.open ('students', 'rb')
	
	alumnList = []
	for t in f.readlines():
		t = t.decode().replace('\n','').split (',')
		
		t = [t[0], ','.join(t[1::])]
		alumnList.append (t)
	
	f.close ()
	
	# Read stdin
	stdin = iter(sys.stdin.readlines())
	stdin.__next__ ()
	# OR
	#stdin = [line.rstrip() for line in open('stdin.txt')] # ERASE FIRST LINE OF FILE
	#
	
	stdin = [','.join( t.split(',') ) for t in stdin]
	
	caseCounter = 1
	
	for stdinElem in stdin:
		sys.stdout.write ("Case #%d: " % caseCounter)
		caseCounter += 1
		
		result = [t[0] for t in alumnList if t[1] == stdinElem.strip()]
		result = sorted (result)
		
		if not result:
			print ('NONE')
		else:
			print (','.join(result))

if __name__ == '__main__':
	main ()
