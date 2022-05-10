# quiqCodingChallenge
Coding challenge for the quip interview process

Since the files are provided via the commandline, serialization was not required like it would be if I was using a REST api to access the .json data.

As a result I was able to directly load the data from both files into a python list. From there I split the list and converted into two sets. I returned the elements that are unique to each set in a list called difference. I took the length of the list difference to get the number of unique elements to each file and used conditional statements to determine the float value which indicates similarity. 

Additionaly for more output I created several print statements for testing that are nested under conditionals which checks the flag variable verboseFlag. 

Language used: 
Python 3.0

Libraries used:
argparse(allows access to commandline args)
