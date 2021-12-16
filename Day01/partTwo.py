
import sys

inputFilename = sys.argv[1]


def main():

    inputFile = open(inputFilename)

    count = 0
 
    list = []

    for line in inputFile:
            line = int(line)
            print("Hallo")
            list.append(int(line))
            
            if(len(list) > 3):

                last4 = int(list[-2]) + int(list[-3]) + int(list[-4])
                last3 = int(list[-1]) + int(list[-2]) + int(list[-3])

                #print(last4, list[-2], list[-3], list[-4])
                #print(last3, list[-1], list[-2], list[-3])

                print(last4)
                print(last3)

                if(int(last4) < int(last3)):
                    print("Count: ", count)
                    count += 1 
                    print("Test")
                print("\n")

    print(count)


main()
