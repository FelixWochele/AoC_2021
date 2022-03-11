import sys

inputFilename = sys.argv[1]


fieldSize = 1000

field = [[0 for x in range(fieldSize)] for x in range(fieldSize)]

def main():

        inputFile = open(inputFilename)

        for line in inputFile: 

            #Parse
            splited = line.split()
            first = splited[0]
            second = splited[2]
            y1 = int(first.split(",")[0])
            x1 = int(first.split(",")[1])
            y2 = int(second.split(",")[0])
            x2 = int(second.split(",")[1])

            #tauschen falls falsch rum
            if(x2 < x1 or y2 < y1):
                temp = x1
                x1 = x2
                x2 = temp
                temp = y1
                y1 = y2
                y2 = temp

            diff = 0

            #Two cases hor/ver
            if(x1 == x2):
                diff = y2 - y1 + 1

                for i in range(diff):
                    field[x1][y1 + i] = field[x1][y1 + i] + 1

            elif(y1 == y2):
                diff = x2 - x1 + 1

                for i in range(diff):
                    field[x1 + i][y1] = field[x1 + i][y1] + 1

        count = 0
        for i in range(fieldSize):
            for j in range(fieldSize):
                if (field[i][j] >= 2):
                    count = count + 1

        print(count)

main()

