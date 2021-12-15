
import sys

inputFilename = sys.argv[1]



def main():

	inputFile = open(inputFilename)

	count = 0
	lastLine = 0

	for line in inputFile:
		line = int(line)

		if(line > lastLine): count = count + 1 

		lastLine = line

	print(count)


main()
