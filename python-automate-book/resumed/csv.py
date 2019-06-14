################ Lendo Arquivo ##########################

import csv

exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
for row in exampleReader:
	print('Row #' + str(exampleReader.line_num) + '' + str(row))



############### Writing #######################

O metodo writerow aceita argumentos do tipo list 

import csv

outputFile = open('outputFile.csv', 'w')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam','eggs','bacon','ham'])
outputWriter.writerow(['Hello, word!','eggs','ham','bacon'])
outputWriter.writerow([1,2,3.1231432,4])
outputFile.close()


file = csv.reader(open('outputFile.csv'))
for f in file:
	print('Row: ' + str(file.line_num) + str(f))

############# Usando delimitadores ######################

para separar as celulas com tabulacao ao inves de virgula e para as linhas
terem espacamento duplo usa o delimiter e lineterminator


import csv

csvFile = open('example.csv','w')
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
csvWriter.writerow(['apples', 'oranges','grapes'])
csvWriter.writerow(['apples', 'oranges','grapes'])
csvFile.close()

csvFile = csv.reader(open('example.csv','r'))
for c in csvFile:
	print('Row: ' + str(csvFile.line_num) + str(c))