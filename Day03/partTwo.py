
import sys

inputFilename = sys.argv[1]





def main():

        dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0}
        normal  = 0
        inverse = 0

        inputFile = open(inputFilename)

        list = []
        listMain = []

        for line in inputFile: 
                if(line != "\n"): 
                       listMain.append(line)

        list = listMain

        for i in range(12):
                
                for d in dict:
                        dict[d] = 0

                if(len(list) > 1): 
                        for line in list:

                                if(line and line != "\n"):
                                        for j in range(12):     
                                                if(int(line[j]) == 0):
                                                        dict[j]  -= 1
                                                else:
                                                        dict[j] += 1
                        if(dict[i] < 0):
                                
                                list = [k for k in list if int(k[i]) == 0]

                        else:
                                list = [k for k in list if int(k[i]) == 1]
        

        erg1 = list[0]
        print(erg1)

        list = listMain

        for line in inputFile: 
                
               list.append(line)

        
        for i in range(12):

                for d in dict:
                        dict[d] = 0

                if(len(list) > 1):
                        for line in list:

                                if(line and line != "\n"):
                                        for j in range(12):     
                                                if(int(line[j]) == 0):
                                                        dict[j]  -= 1
                                                else:
                                                        dict[j] += 1
                            
                        if(dict[i] < 0):
                                
                                list = [k for k in list if int(k[i]) == 1]

                        else:
                                list = [k for k in list if int(k[i]) == 0]
        
 
        erg2 = list[0]
        print(erg2)
        print(int(erg1, 2) * int(erg2, 2))

main()

