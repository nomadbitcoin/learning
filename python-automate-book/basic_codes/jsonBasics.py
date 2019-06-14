#!/usr/bin/python3


###################### Lendo JSON com a função loads() ###############################
import json

stringsOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'

jsonDataAsPythonValue = json.loads(stringsOfJsonData)
print(jsonDataAsPythonValue)

'''
	após importar o modulo json, podemos chamar loads() e passar-lhe uma string com dados JSON.
	Observe que as strings JSON sempre utilizam aspas duplas. Esses dados serão retornados na forma
	de um dicionario Python. Os dicionarios Python não são ordenados, portando os pares chave-valor poderão aparecer
	em uma ordem diferente quando jsonDataAsPythonValue for exibido. 
'''


###################### Escrevendo JSON com a função dumps() ###############################

import json

'''
	A função json.dumps() traduzirá um valor Python em uma string de dados formatada em JSON
'''

pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}

stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)

'''
O valor pode corresponder somente a um dos seguintes tipos de dados básicos do Python: dicionarios, lista, inteiro, ponto flutuante, string, booleano ou None.
'''

###################### Acessando dados atuais de previsao do tempo ###############################
