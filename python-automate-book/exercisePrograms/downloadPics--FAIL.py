#!/usr/bin/env python3
#download de todas as tirinhas XKDC 
import requests, os, bs4

url = 'https://xkcd.com/2065/'		#url inicial

os.makedirs('xkdc', exist_ok=True)	#armazena as tirinhas em /root/prog/python/web/xkdc
while not url.endswith('#'):
	#faz downlad de uma pagina
	print('Downloading page %s...' % url)
	res = requests.get(url)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text, features='lxml')

	#Encontra o URL da imagem da tirinha.
	comicElem = soup.find_all('img')
	#comicElem = soup.select('#comic img')
	if comicElem == []:
		print('i have')
		print(comicElem)
		print('Could not find comic image.')
		break
	else:
		comicUrl = 'http://xkdc.com' + comicElem[0].get('src')
		print(comicUrl)

	#Faz o download da imagem
	print('Downloading image %s...' % (comicUrl))
	res = requests.get(comicUrl)
	res.raise_for_status()

	#Salva a imagem em /root/prog/python/web/
	imageFile = open(os.path.join('xkdc',os.path.basename(comicUrl)), 'wb')
	for chunk in res.iter_content(100000):
		imageFile.write(chunk)
	imageFile.close()

	#Obtem o url do botao Prev
	linkPrev = soup.find_all('a', {'rel': True})
	if linkPrev == []:
		print('Could not find url prev.')
		break
	else:
		url = 'http://xkdc.com' + linkPrev[1].get('href')
		
print('Done.')