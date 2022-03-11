import sys

inputFilename = sys.argv[1]

main = []

day = 256
count = 0
dict = {}

def main():
    count = 0

    inputFile = open(inputFilename)

    #parse input
    for line in inputFile:
        main = line.split(",")
        print("Init: ",  main)

    #Null values   
    for p in range(10):
        dict[p] = 0

    #Insert values in the dict
    for k in range(len(main)):
        dict[int(main[k])] = dict[int(main[k])] + 1

    for i in range(day):

        temp = dict[0]

        #-1
        for x in range(8):
            dict[x] = dict[x + 1]
        dict[8] = 0

        #0 -> 6/8
        dict[6] = temp + dict[6]

        if(temp != 0):
            for z in range(temp):
                dict[8] = dict[8] + 1 

        print(dict)
    
    count = 0
    for t in range(8):
        count = count + dict[t]

    print(count)

main()