# allows for cmd line args
import argparse
#parses the json
import json
# statistical analysis
import pandas

#main
def main():
    # output flag for testing
    verboseFlag = True

    resList = []
    #instantiate the argparse object
    jsonParser = argparse.ArgumentParser()

    # allows the reading in of files from cmdline
    # if these arguments aren't included then an error is displayed to the user
    jsonParser.add_argument('files', type=argparse.FileType('r'), nargs='+')



    # allows access to files
    args = jsonParser.parse_args()

    resList.append(parseCMDLineFileArg(args))

    if verboseFlag == True:
        print("Output in main")
        print("---------------------------")
        print(resList)
        print("---------------------------")
        print("End of output in main")





# parses the cmd line argument and returns
def parseCMDLineFileArg(args):
    verboseFlag = False
    fileList = []
    fpartition1 = []
    fpartition2 = []
    returnList = []


    for file in args.files:
        for char in file:
            fileList.append(char)

    halfwaySplice = len(fileList)//2

    fpartition1 = fileList[:halfwaySplice]
    fpartition2 = fileList[halfwaySplice:]

    if verboseFlag == True:
        print("output in method: parseCMDLineFileArg")
        print("------------------")
        #print(fileList)
        print("------------------")

    fileOneDF = pandas.read_json(path_or_buf=fpartition1, orient='columns')
    fileTwoDF = pandas.read_json(path_or_buf=fpartition2, orient='columns')

    print(fileOneDF)



def displayResult(JsonPair):
    pass






if __name__=='__main__':
	main()
