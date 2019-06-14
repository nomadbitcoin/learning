#!/usr/bin/env python3
# abre varios resultados de pesquisa no Google.- Serao passados em linha de comando junto com comando para abrir o programa

import requests, sys, webbrowser, bs4

print('Googling...') #exibe um texto enquando faz download da pagina do Google
res = requests.get('https://google.com/search?q=' + ''.join(sys.argv[1]))
res.raise_for_status()

#Obtem os links dos principais resultados da pesquisa.

soup = bs4.BeautifulSoup(res.text, features='lxml')


#Abre uma aba do navegador para cada resultado.
linkElems = soup.select('.r a')		# vai pegar somente links da classe "r" 
numOpen = min(5,len(linkElems))		# a função interna min() do python retorna o menor argumento inteiro ou float que receber, nesse caso retornara se a busca tiver menos de 5 links como resultado, ou serao apenas 5 caso tenha mais que 5
for i in range(numOpen):
	webbrowser.open('https://google.com' + linkElems[i].get('href'))