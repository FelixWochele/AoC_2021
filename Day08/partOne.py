import sys

inputFilename = sys.argv[1]

count = 0
second = []

def main():

    inputFile = open(inputFilename)

    for line in inputFile:
        first = line.split("|")[1].split()
        second.extend(first)

    count = 0

    for i in second:

        print(i)
        print(decode(i))


        if(len(i) == 7 or len(i) == 4 or len(i) == 2 or len(i) == 3):
            count = count + 1

        """ if(decode(i) == 1 or decode(i) == 4 or decode(i) == 7 or decode(i) == 8):
            count = count + 1
            print("--------------")  """

    print(count)


def decode(chars):
    number = -1
    sort = sorted(chars)

    if(sort == sorted("abcefg")):
        number = 0
    if(sort == sorted("cf")):
        number = 1
    if(sort == sorted("acdeg")):
        number = 2
    if(sort == sorted("acdfg")):
        number = 3
    if(sort == sorted("bcdf")):
        number = 4
    if(sort == sorted("abdfg")):
        number = 5
    if(sort == sorted("abdefg")):
        number = 6
    if(sort == sorted("acf")):
        number = 7
    if(sort == sorted("abcdefg")):
        number = 8
    if(sort == sorted("abcdfg")):
        number = 9

    return number


main()