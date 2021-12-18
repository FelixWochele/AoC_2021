
import sys

inputFilename = sys.argv[1]





def main():

        inputFile = open(inputFilename)

        bingoNumbers = []
        bingoField = [[]]
        listOfFields = []
        i = 0
        delCount = 0
            
        bingoNumbers = inputFile.readline().split(",")

        #Put the Bingo Fields (2d-A) in a list
        for line in inputFile:
                if(line == "\n"):
                        listOfFields.append(bingoField)
                        bingoField = []
                elif(line):
                        bingoField.append(line.split())

        listOfFields.append(bingoField)
       
        ibingoNumber = 0
        print(bingoNumbers)
        for bingoNumber in range(len(bingoNumbers)):

                ibingoNumber = bingoNumbers[bingoNumber]
                print("BingoNummer: " , ibingoNumber)
            

                if(len(listOfFields) == 2 or len(bingoNumbers) - 1 == bingoNumber):
                        print("Ende")
                        print(listOfFields[1])
                        winner(listOfFields[1], int(ibingoNumber))

                #Bingo Nummer setzte
                listOfFields = [[[99 if int(y) == int(ibingoNumber) else y for y in row ] for row in x ] for x in listOfFields]
                #Prüfen horizontal
                count = 0 
                for field in range(len(listOfFields)):
                        if(listOfFields[field]):
                                for row in range(len(listOfFields[field])):
                                        for number in range(len((listOfFields[field])[row])):
                                                if(int(((listOfFields[field])[row])[number]) == int(99)):
                                                        count += 1
                                                else:
                                                        count = 0
                                                if(count > 4):
                                                        delCount = field
                                                        break
                                        count = 0


                #Prüfen vertikal
                count = 0 
                for field in range(len(listOfFields)):
                        if(listOfFields[field]):
                                for number in range(len((listOfFields[field])[0])):
                                        for row in range(len((listOfFields[field])[row])):
                                                if(int(((listOfFields[field])[row])[number]) == int(99)):
                                                        count += 1
                                                else:
                                                        count = 0
                                                if(count > 4):
                                                        delCount = field
                                                        break
                                        count = 0

                if(delCount > 0):
                        del listOfFields[delCount]
                        delCount = 0
                print(len(listOfFields))

        for bingoField in listOfFields: 
            print(bingoField)


def winner(board, bingoNumber):
        erg = 0
        for row in range(len(board)):
            for number in range(len(board[row])):
                        if (int((board[row])[number]) != int(99)):
                                print(int((board[row])[number]))
                                erg += int((board[row])[number])

        print("\n", erg, "   ", bingoNumber)
        print((erg - bingoNumber) * bingoNumber)
        sys.exit()


main()

