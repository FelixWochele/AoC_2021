
import sys

inputFilename = sys.argv[1]





def main():

        inputFile = open(inputFilename)

        bingoNumbers = []
        bingoField = [[]]
        listOfFields = []
        i = 0
            
        bingoNumbers = inputFile.readline().split(",")

        #Put the Bingo Fields (2d-A) in a list
        for line in inputFile:
                if(line == "\n"):
                        listOfFields.append(bingoField)
                        bingoField = []
                elif(line):
                        bingoField.append(line.split())

        listOfFields.append(bingoField)
        
        for bingoNumber in bingoNumbers:
                print(bingoNumber)

        for bingoNumber in bingoNumbers:

                print("#############################################################", bingoNumber)

                #Bingo Nummer setzte
                listOfFields = [[[99 if int(y) == int(bingoNumber) else y for y in row ] for row in x ] for x in listOfFields]
                #Prüfen horizontal
                count = 0 
                for field in range(len(listOfFields)):
                        if(listOfFields[field]):
                                for row in range(len(listOfFields[field])):
                                        for number in range(len((listOfFields[field])[row])):
                                                print(int(((listOfFields[field])[row])[number]), int(bingoNumber))
                                                if(int(((listOfFields[field])[row])[number]) == int(99)):
                                                        count += 1
                                                else:
                                                        count = 0
                                                if(count > 4):
                                                        print("\n",bingoNumber)
                                                        winner(listOfFields[field], int(bingoNumber))
                                                        sys.exit()
                                        count = 0


                #Prüfen vertikal
                count = 0 
                for field in range(len(listOfFields)):
                        if(listOfFields[field]):
                                for number in range(len((listOfFields[field])[0])):
                                        for row in range(len((listOfFields[field])[row])):
                                                print(int(((listOfFields[field])[row])[number]), int(bingoNumber))
                                                if(int(((listOfFields[field])[row])[number]) == int(99)):
                                                        count += 1
                                                else:
                                                        count = 0
                                                if(count > 4):
                                                        winner(listOfFields[field], bingoNumber)
                                                        sys.exit() 
                                        count = 0

        for bingoField in listOfFields: 
            print(bingoField)


def winner(board, bingoNumber):
        print(bingoNumber) 
        erg = 0
        for row in range(len(board)):
            for number in range(len(board[row])):
                        if (int((board[row])[number]) != int(99)):
                                print(int((board[row])[number]))
                                erg += int((board[row])[number])
        print(erg * bingoNumber)



main()

