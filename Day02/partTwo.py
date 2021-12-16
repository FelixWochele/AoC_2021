
import sys

inputFilename = sys.argv[1]





def main():


        position = 0
        depth = 0
        aim = 0

        inputFile = open(inputFilename)

        for line in inputFile:

                command = line.split()

                if(command):                
                        #print(command[0], command[1])

                        if(command[0] == "forward"):
                                position += int(command[1])
                                depth += aim * int(command[1])

                        elif(command[0] == "up"):
                                aim -= int(command[1])

                        elif(command[0] == "down"):
                                aim += int(command[1])


        print(depth * position)


main()
