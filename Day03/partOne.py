
import sys

inputFilename = sys.argv[1]





def main():

        dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0}
        normal  = 0
        inverse = 0

        inputFile = open(inputFilename)

        

        for line in inputFile: 
                if(line and line != "\n"):
                        print(line, "\n")

                        for i in range(12):     
                                print(i)
                                #print(line[i], "  i:  ", i)
                                print(line[i], "\n")

                                if(int(line[i]) == 0):
                                        dict[i]  -= 1
                                else:
                                        dict[i] += 1
        print(dict) 

        for i in range(12):
                if(int(dict[11 - i]) > 0):
                        normal += 2 ** i   
                else:
                        inverse += 2 ** i


        print("normal:  ", normal, "\n")
        print("inverse: ", inverse, "\n")
        print(normal * inverse)

main()

