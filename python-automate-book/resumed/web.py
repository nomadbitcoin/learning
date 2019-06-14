webbrowser.open('http://inventwithpython.com/')		''' abre o navegador no link passado'''

requests.get()	''' a função requests.get() aceita uma string contendo URL para download. Ao chamar type() no valor de retorno de requests.get(), voce recebera um objeto Response de retorno.'''
res.raise_for_status()	''' res é um objeto response retornado pelo metodo requests e usando o metodo raise_for_status verificamos se o download ocorreu com sucesso'''
res.iter_content(1000000):	''' iter_content retorna porções de dados. Cada porção tem o tipo de dados bytes e é possivel especificar quantos bytes cada porção terá, cem mil bytes geralmente é um bom tamanho'''

noStarchSoup = bs4.BeautifulSoup(res.text, features = "lxml") 		''' cria um objeto BeautifulSoup para ser tratado o codigo html, apos ter um objeto BeautifulSoup podera usar metodos para encontrar partes especificas de um documentos HTML.'''
Seletores para objetos BeautifulSoup - Metodos Html 

soup.select('p')				''' Todos os paragrafos'''
soup.select('div')				''' Todos os elementos de nome <div> '''
soup.select('#author')			''' O elemento com um atributo id igual a author '''
soup.select('.notice') 			''' Todos os elementos que utilizem um atributo class de CSS chamado notice ''' 
soup.select('div span') 		''' Todos os elementos de nome <span> que estejam em um elemento chamado <div>.'''
soup.select('div > span')		''' Todos os elementos de nome <span> que estejam diretamente em um elemento chamado <div>, sem que haja outros elementos intermediarios'''
soup.select('input[name]')		'''	Todos os elementos de nome <input> que tenham um atributo name com qualquer valor.'''
soup.select('input[type="button"]')		''' Todos os elementos de nome <input> que tenham um atributo chamado type com o valor button'''

Os elementos podem ser combinados:
soup.select('p #author') corresponderá a qualquer elemento que tenha um atributo id igual a author, desde que tambem esteja dentro de um elemento <p>

O metodo select() retornará uma lista de objetos Tag, 
a lista conterá um objeto Tag para cada correspondencia feita no HTML do objeto BeautifulSoup. 
Os valores de tag podem ser passados para a função str() para que as tags HTML que representam possam ser mostradas. 
Os valores de Tags tambem tem um atributo attrs que mostra todos os atributos HTML da tag na forma de um dicionario.





...............................................................
...............................................................
...............................................................
...............................................................
...............................................................
...............................................................
###############################################################

#mapw.py - incia o mapa no navegador usando um endereço da linha de comando ou clipboard.
import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
	#obtem o endereço da linha de comando 
	adress = ''.join(sys.argv[1:])		#a variavel sys.argv armazena uma lista contendo o nome de arquivo do programa e os argumentos de linha de comando. Se essa lista contiver mais informações além do nome do arquivo, len(sys.argv) será avaliado como um inteiro maior do que 1, o que quer dizer que argumentos de linha de comando foram fornecidos.
										#join transforma tudo em uma lista de string, passando [1:] ele desconsidera o primeiro valor de string pois nao queremos lidar com o nome do programa que foi passado como primeira string e o argumento como segunda string na linha de comando
else:
#obtém o endereço do clipboard.
	adress = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + adress)

...............................................................
...............................................................
...............................................................
...............................................................
...............................................................
...............................................................
###############################################################

import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res))		''' retorna o tipo Response do objeto res'''
print(len(res.text))	''' retorna quantos caracteres tem o objeto'''
print(res.text[:250])	''' retorna uma string ate do caractere 0 o caractere 250'''

...............................................................
...............................................................
...............................................................
...............................................................
...............................................................
...............................................................
###############################################################

import requests
res = requests.get('https://automatetheboringstuff.com/page_that_does_not_exist')
try:
	res.raise_for_status()
except Exception as exc:
	print('There was a problem %s' % (exc))

...............................................................
...............................................................
...............................................................
...............................................................
...............................................................
...............................................................
###############################################################

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')		''' vai abrir o arquivo em modo de escrita binario para salvar informações de Unicode'''
for chunk in res.iter_content(1000000):			''' pega porções de bytes'''	
	playFile.write(chunk)						''' chama write para escrever o que copiou em cada interação do loop'''
playFile.close()

...............................................................
...............................................................
...............................................................
...............................................................
...............................................................
...............................................................
###############################################################


import requests, bs4
res = requests.get('https://www.nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, features = "lxml")
print(type(noStarchSoup))

...............................................................
...............................................................
...............................................................
...............................................................
...............................................................
...............................................................
###############################################################


import bs4
exampleFile = open('/root/prog/python/web/example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), features='lxml')
elems = exampleSoup.select('#author')
print(type(elems[0]))
print(len(elems))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)



Esse código extrairá o elemento com id="author" de nosso html de exemplo.
Usamos select('#author') para retornar uma lista contendo todos os elementos com id="author".
Armazenamos essa lista de objetos Tag na variavel elems e len(elems) nos informa que há um objeto Tag na lista, ou seja, ouve uma correspondencia.
Chamar getText() no elemento fará o texto desse elemento ser retornado, isto é, o HTML interno.
O texto de um elemento é o conteudo entre as tags de abertura e de fechamento
Passar o elemento para str() fará uma string ser retornada com as tags de abertura e de fechamentos e o texto do elemento. 
Por fim, attrs nos fornece um dicionario com o atributo 'id' do elemento e o valor desse atributo, ou seja, 'author'

...............................................................
...............................................................
...............................................................
...............................................................
...............................................................
...............................................................
###############################################################

import bs4
soup = bs4.BeautifulSoup(open('/root/prog/python/web/example.html'), features='lxml')
spanElem = soup.select('span')[0]
print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.get('some_nonexistente_addr') == None)
print(spanElem.attrs)



Nesse caso usamos select() para encontrar todos os elementos <span> e enta armazenamos o primeiro elemento correspondente em spanElem.
Passar o nome de atributo 'id' para get() faz o valor do atributo, ou seja 'author', ser retornado

...............................................................
...............................................................
...............................................................
...............................................................
...............................................................
...............................................................
###############################################################
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

...............................................................
...............................................................
...............................................................
...............................................................
...............................................................
...............................................................
###############################################################

