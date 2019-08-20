import yaml
import itertools

with open("conditions.yml", 'r') as stream:
    conditions = yaml.safe_load(stream)
    print("Conditions =>", conditions)

parameters = conditions['parameters']
invalid = list(conditions['invalid'])

# print(len(invalid))
print("Parameters 2nd one => ", parameters['age'])

paramNames = []

# getting Names of Parameters
for names in parameters:
    paramNames.append(names)

for k, v in parameters.items():
    firstParameter = v
    break

print("FirstParameter => ", firstParameter)
print("FirstParameter[0] => ", firstParameter[0])
print("FirstParameter Length => ", len(firstParameter))

allCombinations = []
iterationsOfParameters = len(paramNames) - 1

a = 0
b = 1
for a in range(len(firstParameter)):
    allCombinations.append([])
    allCombinations[a].append([firstParameter[a]])
    for b in range(iterationsOfParameters):
        allCombinations[a].append(parameters[paramNames[b+1]])

print("All => ", allCombinations)


print("ParamNames : ", paramNames)

print("Parameters =>", parameters)
print("Invalid =>", invalid)
