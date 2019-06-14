#!/usr/bin/env python3
#work with directory

os.getcwd()										''' mostra o diretorio atual'''
os.chdir('/')									''' muda o diretorio atual para o argumento passado'''	
os.makedirs('/root/programming/teste') 				'''create paste/directory'''
os.makedirs('/root/teste/teste') 					'''create all directory specified'''


os.path.abspath(path)						'''retornara uma string com o path absoluto referente ao argumento maneira facil de converter path relativo em path absoluto'''
os.path.isabs()								'''retornara True se o argumento for um path absoluto e False se for relativo'''
os.path.relpath(path, incio)				'''retornara uma string contendo um path relativo ao path inicio para path. se inicio nao for especificado, o diretorio de trabalho atual sera usado como inicio'''

os.path.basename(path)							'''mostra tudo que esta após a ultima barra'''
os.path.dirname(path)							'''mostra tudo que esta antes da ultima barra'''

os.path.split(variable)						'''retorna uma tupla com os valores de path e de nome base(nome do arquivo)'''
variable.split(os.path.sep) 					'''retorna uma tupla com valores de endereço do arquivo'''

os.path.getsize(path)			''' retornara o tamanho em bytes do arquivo no argumento path'''
os.listdir(path)				''' retornara uma lista de strings com nomes de arquivo para cada arquivo argumento path'''

os.path.exists(path)			''' retornara True se o arquivo ou a pasta referenciada no argumento existir e False caso contrario'''
os.path.isfile(path)			''' retornara True se o argumento referente ao path existir e for um arquivo e retornara False caso contrario'''
os.path.isdir(path)				''' retornara True se o argumento referente ao path existir e for uma pasta e retornara False caso contrario'''

open()					''' para que o um objeto file seja retornado'''		''' open(r'')passar r como segundo argumento nao abrira em leitura default'''
read() ou write()		''' chamar read ou write no object file'''
close()					''' fechar o arquivo chamando o metodo close no objeto file'''

variable_File = open('/', 'w')					''' w de write, vai escrever no arquivo e sempre ira escrever em cima do que tinha antes'''
variable_File = open('/', 'a')					''' a de adicionar, vai adicionar ao arquivo, mantendo assim o que tinha antes'''

import shutil
shutil.copy('spam.txt', 'automate/delicious')		'''shutil.copy copia o arquivo do primeiro argumento para o local do segundo argumento e caso seja um nome de arquivo, será o nome do novo arquivo após copiado '''
shutil.copytree('local', 'destino') 				''' copia a pasta e todas as subpastas passadas no primeiro argumento para o segundo argumento, a própria função criará a pasta destino '''

shutil.move('local', 'destino')							''' moverá o arquivo ou a pasta no path origem para o path destino e retornará uma string com o path absoluto da nova localidade'''
shutil.move('bacon.txt', 'automate/new_bacon.txt')		''' moverá o arquivo e renomeará'''

os.unlink(path)				''' apagará o permanentemente o arquivo em path '''
os.rmdir(path)				''' apagará permanentemente a pasta em path. Essa pasta deve estar vazia'''
os.rmtree(path) 			''' apagará permanentemente a pasta e todos os arquivos que estiverem dentro dela em path'''
send2trash.send2trash('bacon.txt')		''' apagará o arquivo enviando-o para lixeira'''

os.walk('/root/new')		''' os.walk pode ser usada em um loop para percorrer uma arvore de diretorio, retornará três valores a cada interação pelo loop, uma string com o nome da pasta atual, uma lista de strings com as pastas da pasta atual, uma lista de strings com arquivos da pasta atual (possivelmente isso é regra apenas para esse programa que criei agora)'''

exampleZip = zipfile.ZipFile('archivesbook.zip')
exampleZip.namelist()														''' namelist retorna uma lista com os arquivos dentro do zip'''
spamInfo = exampleZip.getinfo('automate_online-materials/zophie.png')		''' getinfo pega informações sobre itens dessa lista que foi retornada '''															
spamInfo.compress_size												''' compacta o arquivo da lista do qual foi solicitado informações '''
exampleZip.close()			'''Um Objeto ZipFile tem um metodo namelist() que retorna uma lista de strongs com todos os arquivos e pastas no zip, essas strings podem ser passadas ao metodo getinfo() de ZipFile para retornar um objeto ZipInfo associado a esse arquivo em particular. os objetos ZipInfo tem seus próprios atributos, como file_size e compress_size em bytes, que armazenam inteiros relativos ao tamanho original do arquivo e ao tamanho compactado '''

exampleZip = zipfile.ZipFile('archivesbook.zip')
exampleZip.extractall('destino/create paste or empty to extract here')			''' extrair arquivos'''
exampleZip.extract('archive')	''' extrair um unico arquivo do ZipFile'''
exampleZip.close()	

newZip = zipfile.ZipFile('new.zip', 'w')	''' abrir o objeto ZipFile passando "w" como segundo argumento '''
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)	''' passar um path para o metodo write() de um objeto ZipFile, o python compactará o arquivo nesse path e o adicionará ao arquivo ZIP, o primeiro argumento do metodo write() é uma string que contem o nome do arquivo a ser adicionado, o segundo argumento é o tipo de compactação onde zipfile.ZIP_DEFLATED (algoritmo de compactação deflate que funciona bem para todos os tipos de dados)'''
newZip.close()






#-------------------------------------##
shelfFile = shelve.open('mydata')	''' save variables on archives'''
cats = ['Zophie','Pooka','Simon']	''' can use this variables values in other programs'''
shelfFile['cats'] = cats
shelfFile.close()

saved myCats.py 			''' created other file myCats.py and can possible import to my program'''
import myCats
print(myCats.cats)			''' have a two lists and here i imported the first list'''	
print(myCats.bob)			''' here i imported the second list'''
print(myCats.bob[0])		''' here i imported de first item in the second list'''

############################################################

import os
print(os.getcwd())	#show directory atual
os.chdir('/root/programming/python/blockchain') #change directory atual to '/directory'
print('directory changed to: ',os.getcwd()) 

############################################################

import os
os.makedirs('/root/programming/teste') 					'''create paste/directory'''
os.makedirs('/root/teste/teste') 						'''create all directory specified'''
print('created directory: /root/teste/teste')

############################################################
import os
print(os.path.abspath('./'))	'''é um diretorio a partir do qual executo agora, o qual não é absoluto e sim relativo'''
print(os.path.isabs('/root/python'))	#é um diretorio absoluto
print(os.path.isabs(os.path.abspath('.'))) #transforma o path '.' em absoluto

import os
print(os.path.relpath('/root','/'))	#nao entendi direito
print(os.path.relpath('/root','/programming/python/automate'))
print(os.getcwd())		
#############################################################

import os
path = '/root/Documents/books/aerodinamica nao estacionaria.pdf'
print(os.path.basename(path))							'''mostra tudo que esta após a ultima barra'''
print(os.path.dirname(path))							'''mostra tudo que esta antes da ultima barra'''

#############################################################

calcFilePath = '/root/Documents/books/aerodinamica nao estacionaria.pdf'
print(os.path.split(calcFilePath))						'''retorna uma tupla com os valores de path e de nome base(nome do arquivo)'''
print(calcFilePath.split(os.path.sep)) 					'''retorna uma tupla com valores de endereço do arquivo'''

#############################################################

import os
print(os.path.getsize('/root/Documents/books/aerodinamica nao estacionaria.pdf'))		#informa tamanho do arquivo passado no argumento
print(os.listdir('/root/Desktop'))			#lista o diretorio passado no argumento

	####################++++++++++++++++++##############################
	#calculate size of all archives inside the directory
	import os
	totalSize = 0
	for filename in os.listdir('/root/Documents/books'):
		totalSize = totalSize + os.path.getsize(os.path.join('/root/Documents/books',filename))
	print(totalSize)

##############################################################

import os
print(os.path.exists('/root/good.mp3'))		#retorna True se o arquivo ou diretorio passado no argumento existir
print(os.path.exists('/baby'))				#retorna False se o arquivo ou diretorio nao existir
print(os.path.isdir('/root'))				#retorna True se o argumento passado for um diretorio e existir
print(os.path.isdir('/nope'))				#retorna False se o diretorio nao existir 
print(os.path.isfile('/root/good.mp3'))		#retorna True se o argumento passado for um arquivo e existir
print(os.path.isfile('/root'))				#retorna False se o argumento passado nao for um arquivo

##############################################################

import os									''' ler arquivo'''
helloFile = open('/root/hello.txt')
helloContent = helloFile.read()
print(helloContent)

##############################################################
	
import os								''' separar linhas em strings diferentes'''
sonnetFile = open('/root/hello.txt')
print(sonnetFile.readlines())

##############################################################

import os
baconFile = open('/root/programming/python/workwithfiles/bacon.txt', 'w')		#vai escrever no arquivo em cima do que tinha antes
baconFile.write('Hello Everybody \n')
baconFile.close()

baconFile = open('/root/programming/python/workwithfiles/bacon.txt', 'a')		#vai adicionar ao arquivo a partir do que tinha antes
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

baconFile = open('/root/programming/python/workwithfiles/bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)

##############################################################

import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie','Pooka','Simon']
shelfFile['cats'] = cats
shelfFile.close()
print(cats)

import shelve
shelFile = shelve.open('mydata')
print(list(shelFile.values()))
shelFile.close()

##############################################################

import send2trash
baconFile = open('bacon.txt', 'a')	#cria o arquivo
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
send2trash.send2trash('bacon.txt')

###############################################################

import os
for folderName, subfolders, filenames in os.walk('/root/new'):
	print('The current folder is ' + folderName)
	for subfolder in subfolders:
		print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
	for filename in filenames:
		print('FILE INSIDE ' + folderName + ': ' + filename)
print('')

###############################################################

import zipfile, os
os.chdir('/root/prog/python/workwithfiles/')
exampleZip = zipfile.ZipFile('archivesbook.zip')
exampleZip.namelist()														''' namelist retorna uma lista com os arquivos dentro do zip'''
spamInfo = exampleZip.getinfo('automate_online-materials/zophie.png')		''' getinfo pega informações sobre itens dessa lista que foi retornada '''
print(spamInfo)																
print(spamInfo.compress_size)												''' compacta o arquivo da lista do qual foi solicitado informações '''
exampleZip.close()									

###############################################################

import zipfile
newZip = zipfile.ZipFile('/root/prog/python/workwithfiles/new.zip', 'w')
newZip.write('/root/prog/python/workwithfiles/spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()

##############################################################


