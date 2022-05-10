# allows for cmd line args
import argparse



#main
def main():


    #instantiate the argparse object
    jsonParser = argparse.ArgumentParser()

    # allows the reading in of files from cmdline
    # if these arguments aren't included then an error is displayed to the user
    jsonParser.add_argument('files', type=argparse.FileType('r'), nargs='+')



    # allows access to files
    args = jsonParser.parse_args()

    returnInt = parseCMDLineFileArg(args)

    dispRes(returnInt)










def dispRes(intResult):
    print("-----File comparison integer----")
    print("These two files have a similarity index of:", intResult)
    print("------End of json comparison----")
# parses the cmd line argument and returns
def parseCMDLineFileArg(args):

    # set to true to see full output of values
    verboseFlag = False

    # cmd line args take both files in as a concatenated list
    fileList = []

    # As a result must splice
    fpartition1 = []
    fpartition2 = []
    similarityInt = 0

    # convert both files into a concatenated list
    for file in args.files:
        for char in file:
            fileList.append(char)

    # splice index
    halfwaySplice = len(fileList)//2
    #spliced Lists
    fpartition1 = fileList[:halfwaySplice]
    fpartition2 = fileList[halfwaySplice:]
    # converted to sets to determine intersectionality
    setPart1 = set(fpartition1)
    setPart2 = set(fpartition2)
    # this list contains the elements that are unique to each set
    difference = list(setPart1.symmetric_difference(setPart2))
    similarityDiff = len(fileList) - len(difference)

    if verboseFlag == True:
        print("---------Sets-----------")
        print("returns all elements that are different")
        print(difference)
        print("the number of unique values decement the float value which r")
        print("----------end Sets----------")

     # if the length of the difference is greater than one or the other split
     # lists than the files have no intersectionality, therefore they are almost completely different
    if len(difference) >= len(fileList):
         similarityInt = 0.0
         return similarityInt


    #otherwise a score other than 0.0 can be assig
    elif len(difference) < len(fpartition1):
       similarityInt = 1.0
       similarityDiff = len(fileList) - len(difference)

       # if the difference has more than 10 objects but less than 15
       # subtract half to indicate that there is a mixed simularity
    if similarityDiff > 10 and similarityDiff < 15:
           similarityInt - 0.5
           return similarity

       # if the non-intersection is less than 10 then subtract 0.0.1 from each
       # divergent element to get the similarity float while index is less than
       # the total difference
    elif similarityDiff < 10:
           similarityInt = 1
           index = 0

           while(index < len(difference)):
               index+=1
               similarityInt - 0.1

           return similarityInt

       # if the difference is 1 or smaller return 1.0
    if len(difference) <=1:
          similarityInt = 1.0
          return similarityInt
    # if none of the comparison checks got entered
    # then 100% intersectionality
    return 1.0

    if verboseFlag == True:
        print("output in method: parseCMDLineFileArg")
        print("------------------")
        print(fpartition1)
        print("------------------")








if __name__=='__main__':
	main()
