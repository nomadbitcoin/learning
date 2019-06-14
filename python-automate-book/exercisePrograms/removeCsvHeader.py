#!/usr/bin/python3
#removeCsvHeader.py - Remove o cabecalho de todos os arquivos CSV no diretorio atual

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

'''
	A chamada os.makedirs criara uma pasta headerRemoved onde serao gravados os arquivos
	Um loop for em os.listdir('.') faz a metade do trabalho, porem o loop incluira todos os arquivos no diretorio de trabalho
portanto inserimos no comeco do loop que se nao terminar com .csv sejam ignorados.
	A instrucao continue faz com que o loop passe para o proximo arquivo quando um arquivo csv nao seja encontrado.
'''

#Percorre todos os arquivos  o diretorio de trabalho atual em um loop.
for csvFilename in os.listdir('.'):
	if not csvFilename.endswith('.csv'):
		continue		#ignora arquivos que nao sejam csv
	print('Removing header from ' + csvFilename + '...')

	#TODO: Le o arquivo CSV (pula a primeira linha).
	csvRows = []
	csvFileObj = open(csvFilename)
	readerObj = csv.reader(csvFileObj)

	for row in readerObj:
		if readerObj.line_num == 1:
			continue		#pula a primeira linha
		csvRows.append(row)	
	csvFileObj.close()

	#TODO: Grava o arquivo csv.
	csvFileObj = open(os.path.join('headerRemoved',csvFilename),'w', newline='')
	csvWriter = csv.writer(csvFileObj)
	for row in csvRows:
		csvWriter.writerow(row)
	csvFileObj.close()




