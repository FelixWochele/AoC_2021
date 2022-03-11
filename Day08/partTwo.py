import sys

inputFilename = sys.argv[1]

second = []
numberList = []

def main():

    inputFile = open(inputFilename)

    for line in inputFile:
        first = line.split("|")[1].split()
        second.append(first)

    count = 0

    for i in second:
        print(i)
        temp = []
        for j in i:
            temp.append(str(decode(j)))
        print(int("".join(temp)))
        numberList.append(int("".join(temp)))

    res = 0
    for z in numberList:
        res = res + z


    print(res)


def decode(chars):
    number = -1
    sort = sorted(chars)


    if(len(sort) == 2):
        number = 1
    elif(len(sort) == 3):
        number = 7
    elif(len(sort) == 5):
        number = 2
    elif(sort == sorted("cdbaf")):
        number = 3
    elif(len(sort) == 4):
        number = 4
    elif(sort == sorted("cagedb")):
        number = 0
    elif(sort == sorted("cdfbe")):
        number = 5
    elif(sort == sorted("cefabd")):
        number = 9
    elif(sort == sorted("cdfgeb")):
        number = 6
    elif(len(sort) == 6):
        number = 9
    elif(sort == sorted("acedgfb")):
        number = 8
    
    return number


main()