import sys

import yaml
import itertools
import csv

count = 0

while count == 0:
    try:
        # get input from arguments passed
        inputFileName = sys.argv[1]
        outputFileName = sys.argv[2]
    except:
        # get User input from console
        print('Enter a Input file Name:')
        inputFileName = input()
        print('Enter a Output file Name:')
        outputFileName = input()

    # adding file extensions as the input file can only be yml and output be csv
    print(inputFileName)
    inputFileName = inputFileName + ".yml"
    outputFileName = outputFileName + ".csv"

    print("Your Input File Name is: ", inputFileName)
    print("Your Output File Name is: ", outputFileName)

    try:
        # getting data from input file to pyyaml format for parsing
        with open(inputFileName, 'r') as stream:
            conditions = yaml.safe_load(stream)
        count = 1
    except:
        print("File Name ", inputFileName,
              " deos not exist. Please create such file or enter the file name properly and try again.")
        sys.exit()

# diving the all input conditions to separate lists
parameters = conditions['parameters']
invalid = list(conditions['invalid'])

paramNames = []

# getting Names of Parameters
for names in parameters:
    paramNames.append(names)

for k, v in parameters.items():
    firstParameter = v
    break

print(firstParameter)
print(paramNames)
allCombinations = []
iterationsOfParameters = len(paramNames) - 1

a = 0
b = 1

# structuring the Parameters for generating conditions.
for a in range(len(firstParameter)):
    allCombinations.append([])
    allCombinations[a].append([firstParameter[a]])
    for b in range(iterationsOfParameters):
        allCombinations[a].append(parameters[paramNames[b + 1]])

invalidCombinations = []

c = 0
d = 1
# structuring invalid conditions to opt out of the final output
for c in range(len(invalid)):
    invalidCombinations.append([])
    invalidCombinations[c].append([invalid[c][paramNames[0]]])
    for d in range(len(invalid[c]) - 1):
        if isinstance(invalid[c][paramNames[d + 1]], list):
            invalidCombinations[c].append(invalid[c][paramNames[d + 1]])
        else:
            invalidCombinations[c].append([invalid[c][paramNames[d + 1]]])

finalList = []
list = []

e = 0
f = 1

print(allCombinations)
print(invalidCombinations)


# function to compare two lists and remove the similar ones
def diff(first, second):
    second = set(second)
    return [item for item in first if item not in second]


# setting up final conditions based on all conditions and invalid conditions
for e in range(len(allCombinations)):
    finalList.append([])

    if allCombinations[e][0] == invalidCombinations[e][0]:
        finalList[e].append(allCombinations[e][0])

        for f in range(len(allCombinations[e])):
            if f == 0:
                continue
            try:
                finalList[e].append(diff(allCombinations[e][f], invalidCombinations[e][f]))
            except:
                finalList[e].append(allCombinations[e][f])

output = []
i = 0
k = 0
# writing all possible conditions to a csv file.
with open(outputFileName, 'w', newline='\n') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(paramNames)
    for i in finalList:
        # making all possible conditions
        output = ["".join(str(x)) for x in itertools.product(*i)]
        for k in range(len(output)):
            outputStr = output[k]
            outputStrFormatted = outputStr.replace("(", "")
            outputStrFormatted2 = outputStrFormatted.replace(")", "")
            outputStrFormatted3 = outputStrFormatted2.replace("'", "")
            outputList = outputStrFormatted3.split(",")

            wr.writerow(outputList)
        output.clear()
    print("Data Written to ", outputFileName)
