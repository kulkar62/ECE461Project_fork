import json

file = open('coverage.json')
covered_lines = 0
total_lines = 0
data = json.load(file)
#print(data.keys())
files = data.get('files')
fileKeys = list(files.keys())
#print(files)
curFile = files.get(fileKeys[0])
#print(curFile)
summary = curFile.get('summary')
covered_lines += summary.get('covered_lines')
total_lines += summary.get('num_statements')



file = open('../coverage/coverage-summary.json')
jestData = json.load(file)
#print(jestData.keys())
jestTotal = jestData.get('total')
#print(jestTotal.keys())
jestStatements = jestTotal.get('statements')
#print(jestStatements.keys())
covered_lines += jestStatements.get('covered')
total_lines += jestStatements.get('total')

coverage = (covered_lines / total_lines) * 100
inputFile = open('pythonResults.txt', 'r')
testData = inputFile.read().splitlines()
passed = int(testData[1]) - int(testData[0])
total = testData[1]


print(f'{passed}/{total} test cases passed. {coverage}% line coverage achieved.');


