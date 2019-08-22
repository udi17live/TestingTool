import yaml
import itertools
import csv

with open("conditions.yml", 'r') as stream:
    conditions = yaml.safe_load(stream)

parameters = conditions['parameters']
invalid = list(conditions['invalid'])

paramNames = []

# getting Names of Parameters
for names in parameters:
    paramNames.append(names)

for k, v in parameters.items():
    firstParameter = v
    break

allCombinations = []
iterationsOfParameters = len(paramNames) - 1

a = 0
b = 1

# structuring the Parameters
for a in range(len(firstParameter)):
    allCombinations.append([])
    allCombinations[a].append([firstParameter[a]])
    for b in range(iterationsOfParameters):
        allCombinations[a].append(parameters[paramNames[b + 1]])

invalidCombinations = []

c = 0
d = 1
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


def diff(first, second):
    second = set(second)
    return [item for item in first if item not in second]


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
with open('conditions.csv', 'w', newline='\n') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(paramNames)
    for i in finalList:
        output = ["".join(str(x)) for x in itertools.product(*i)]
        for k in range(len(output)):
            outputStr = output[k]
            outputStrFormatted = outputStr.replace("(", "")
            outputStrFormatted2 = outputStrFormatted.replace(")", "")
            outputStrFormatted3 = outputStrFormatted2.replace("'", "")
            outputList = outputStrFormatted3.split(",")

            wr.writerow(outputList)
        output.clear()
    print("Data Written conditions.csv")
