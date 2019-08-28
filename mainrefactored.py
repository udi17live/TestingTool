import sys

import yaml
import itertools
import csv
import json


#############
# FUNCTIONS #
#############

# function to Validate Input File
def generate_conditions_array(input_file):
    inputFileExt = input_file.split(".")
    try:
        with open(input_file, 'r') as stream:
            if inputFileExt[1] == "yml":
                conditionsYaml = yaml.safe_load(stream)
                return conditionsYaml
            elif inputFileExt[1] == "json":
                conditionsJson = json.load(stream)
                return conditionsJson
    except:
        print("File you entered is not found!")
        sys.exit()


# function to compare two lists and remove the similar ones
def diff(first, second):
    second = set(second)
    return [item for item in first if item not in second]


# function to generate final list
def generate_final_combinations_list(allCombo, invalidCombo):
    combinationsList = []
    for e in range(len(allCombo)):
        combinationsList.append([])
        if allCombo[e][0] == invalidCombo[e][0]:
            combinationsList[e].append(allCombo[e][0])
            for f in range(len(allCombo[e])):
                if f == 0:
                    continue
                try:
                    combinationsList[e].append(diff(allCombo[e][f], invalidCombo[e][f]))
                except:
                    combinationsList[e].append(allCombo[e][f])
    return combinationsList


# Output file format Validation.
def validate_output_file(output):
    try:
        outputFileExt = output.split(".")
        if outputFileExt[1] == 'csv':
            pass
        else:
            print("Sorry, ", outputFileExt[1].upper(),
                  " extension is not supported for output. Only CSV files are supported.")
            sys.exit()
    except:
        sys.exit()


# Input file format Validation.
def validate_input_file(input):
    try:
        inputFileExt = input.split(".")
        if inputFileExt[1] == 'yml':
            pass
        elif inputFileExt[1] == "json":
            pass
        else:
            print("Sorry, ", inputFileExt[1].upper(),
                  " extension is not supported for input. Only YML and JSON files are supported.")
            sys.exit()
    except:
        sys.exit()


# writing all possible conditions to a csv file.
def generate_output(outputF):
    outputFileExt = outputF.split(".")
    with open(outputF, 'w', newline='\n') as myfile:
        if outputFileExt[1] == "csv":
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
        print("Data Written to ", outputF)


###############
# APPLICATION #
###############

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

validate_input_file(inputFileName)
validate_output_file(outputFileName)

conditions = generate_conditions_array(inputFileName)

paramNames = []
allCombinations = []
invalidCombinations = []
finalList = []
count = 0

parameters = conditions['parameters']
invalid = list(conditions['invalid'])

for k, v in parameters.items():
    paramNames.append(k)
    if count == 0:
        firstParameter = v
    count += 1

# structuring the Parameters for generating conditions.
for a in range(len(firstParameter)):
    allCombinations.append([])
    allCombinations[a].append([firstParameter[a]])
    for b in range(len(paramNames) - 1):
        allCombinations[a].append(parameters[paramNames[b + 1]])

# structuring invalid conditions to opt out of the final output
for c in range(len(invalid)):
    invalidCombinations.append([])
    invalidCombinations[c].append([invalid[c][paramNames[0]]])
    for d in range(len(invalid[c]) - 1):
        if isinstance(invalid[c][paramNames[d + 1]], list):
            invalidCombinations[c].append(invalid[c][paramNames[d + 1]])
        else:
            invalidCombinations[c].append([invalid[c][paramNames[d + 1]]])

finalList = generate_final_combinations_list(allCombinations, invalidCombinations)

generate_output(outputFileName)
