import sys
from tempfile import tempdir

inputFilename = sys.argv[1]

depthMap = []

def main():

    inputFile = open(inputFilename)

    for line in inputFile:
        liste = list(line)
        for i in liste:
            if(i == '\n'):
                liste.remove('\n')
        depthMap.append(liste)

    temp = 0
    dict = {}
    for layer in depthMap:
        for j in range(len(layer)):
            if(layer[i] < layer[i + 1]):
                temp = layer[i]
            elif:


    for layer in depthMap:
        print(layer)

main()