#!/usr/bin/python3
#quickWeather.py - Exibe a prveisão do tempo para uma localidade obtida na linha de comando.

#problem with API Login


import json, requests, sys

#Processa a localidade a partir da linha de comando.
if len(sys.argv) < 2:
	print('Usage: quickWeather.py location')
	sys.exit()
location = ''.join(sys.argv[1:])

'''
	em Python, os argumentos da linha de comando são armazenados na lista sys.argv. Após a linha shebang #! e as instruções import, o programa verifica se há mais de um argumento na linha de comando.
	(Lembra-se de que sys.argv sempre terá pelo menos um elemento sys.argv[0] que contém o nome do arquivo script Python.) Se houver apenas um elemento na lista, o usuario não especificou  localidade na linha de comando e uma mensagem de "uso" será fornecida ao usuario.

	Os argumentos da linha de comando são separados por espaços. O argumento de linha de comando San Francisco, CA fará sys.argv armazenar ['quickWeather.py','San', 'Francisco', 'CA'].
	Sendo assim, chame o método join() para unir todas as strings em sys.argv, exceto a primeira, Armazene essa string resultante dessa uniao em uma variavel chamada location.
'''

#TODO: Faz download dos dados JSON a partir da API openweathermapeatherMap.org
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)

#TODO: Carrega dados JSON em uma variavel Python.
weatherData = json.loads(response.text)
print(weatherData)
sys.exit()

#exibe as descricoes da previsao do tempo.
w = weatherData['list']
print('Current weather in %s' % (location))
print([0]['weather'][0]['main'], '-',w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][1]['main'], '-',w[1]['weather'][1]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][2]['main'], '-',w[2]['weather'][2]['description'])
