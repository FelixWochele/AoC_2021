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

            else:
                
                diff = x2 - x1

                if(diff < 0):
                    diff = diff * -1 
                diff = diff + 1

                if(x1 < x2 and y1 < y2):
                    direction = 4
                elif(x1 > x2 and y1 < y2):
                    direction = 1
                elif(x1 < x2 and y1 > y2):
                    direction = 3
                elif(x1 > x2 and y1 > y2):
                    direction = 2

                for i in range(diff): 
                    if(direction == 4):
                        field[x1 + i][y1 + i] = field[x1 + i][y1 + i] + 1
                    if(direction == 1):
                        field[x1 - i][y1 + i] = field[x1 - i][y1 + i] + 1
                    if(direction == 3):
                        field[x1 + i][y1 - i] = field[x1 + i][y1 - i] + 1
                    if(direction == 2):
                        field[x1 - i][y1 - i] = field[x1 - i][y1 - i] + 1

        count = 0
        for i in range(fieldSize):
            for j in range(fieldSize):
                if (field[i][j] >= 2):
                    count = count + 1

        print(count)

main()

