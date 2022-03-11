import sys

inputFilename = sys.argv[1]

main = []

day = 80

def main():

    inputFile = open(inputFilename)

    for line in inputFile:
        main = line.split(",")
        print("Init: ",  main)
    

    for i in range(len(main)):
        main[i] = int(main[i])

    for i in range(day):

        for j in range(len(main)):
            main[j] = main[j] - 1
            if(main[j] < 0):
                main[j] = 6
                main.append(8)

    print(len(main))


main()