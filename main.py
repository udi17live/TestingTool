import yaml
import itertools


with open("conditions.yml", 'r') as stream:
    conditions = yaml.safe_load(stream)
    # print("Conditions =>", conditions)

parameters = conditions['parameters']
invalid = list(conditions['invalid'])

# print(len(invalid))
# print("Parameters 2nd one => ", parameters['age'])

paramNames = []

# getting Names of Parameters
for names in parameters:
    paramNames.append(names)

for k, v in parameters.items():
    firstParameter = v
    break

# print("FirstParameter => ", firstParameter)
# print("FirstParameter[0] => ", firstParameter[0])
# print("FirstParameter Length => ", len(firstParameter))

allCombinations = []
iterationsOfParameters = len(paramNames) - 1

a = 0
b = 1

# structuring the Parameters
for a in range(len(firstParameter)):
    allCombinations.append([])
    allCombinations[a].append([firstParameter[a]])
    for b in range(iterationsOfParameters):
        allCombinations[a].append(parameters[paramNames[b+1]])

print("All => ", allCombinations)

invalidCombinations = []

c = 0
d = 1
for c in range(len(invalid)):
    invalidCombinations.append([])
    invalidCombinations[c].append([invalid[c][paramNames[0]]])
    for d in range(len(invalid[c]) - 1):
        if isinstance(invalid[c][paramNames[d+1]], list):
            invalidCombinations[c].append(invalid[c][paramNames[d+1]])
        else:
            invalidCombinations[c].append([invalid[c][paramNames[d+1]]])

print("Invalid Combo =>", invalidCombinations)

finalList = []
list = []

e = 0
f = 1
g = 0
h = 0


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





print("Final List => ", finalList)


output = []



i = 0
j = 0
k = 0

for i in finalList:
    output = ["".join(str(x)) for x in itertools.product(*i)]
    print(output)
    output.clear()