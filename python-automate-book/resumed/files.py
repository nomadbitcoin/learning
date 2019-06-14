#!/usr/bin/python3

import os

'''
	Se você passar os valores de string com os nomes individuais dos arquivos e das pastas de seu path
	os.path.join() retornara uma string com um path de arquivo que utilizara os separadores corretos de path para 
	Windows ou Linux
'''
os.path.join('usr', 'bin', 'spam')


############################################################################################

'''
	A função os.path.join() será util se ouver necessidade de criar strings para os nomes de arquivo. Essas strings serão passadas para 
	diversas funções relacionadas a arquivos que serão apresentadas nesse capitulo.
	o Exemplo a seguir une os nomes de uma lista de nomes de arquio no final do n ome de uma pasta:
'''
myFiles = ['accounts.txt','details.csv', 'invite.docx']
for filename in myFiles:
	print(os.path.join('/home/yan/prog/python/workflow', filename))


############################################################################################


'''
	Podemos obter o diretorio de trabalho atual como um valor de string usando a funcao os.getcwd()
	e altera-lo com os.chdir()
	e criar novas pastas com os.makedirs()
'''

print(os.getcwd())
os.chdir('/home')
print(os.getcwd())
os.makedirs('new past')

############################################################################################
'''
Path absoluto é diretorio que sempre começa da raiz

Path relativo é o diretorio relativo ao diretorio de trabalho atual
'''
############################################################################################

####################Lidando com paths absolutos e relativos ###################################

'''
	Chamar os.path.abspath(path) retornara uma string com o path absoluto referente ao argumento
	Chamar os.path.isabs(path) retornara True se o argumento for um path absoluto e False se for um path relativo.

	Chamar os.realpath(path, inicio) retornara uma string contendo um path relativo ao path inicio para path passado como primeiroa argumento. Se inicio
	nao for especificado, o diretorio de trabalho atual sera usado como path de inicio.
'''

print(os.path.abspath('.'))		#retorna o caminho do diretorio de trabalho atual desde o diretorio raiz


dire = os.getcwd()
print(os.path.isabs(dire))		#True se for path absoluto e False se for Relativo
print(os.path.isabs('.'))

print('')
print(os.path.realpath('/prog/new past',''))

############################################################################################

'''
	Chamar os.path.dirname(path) retornara uma string contendo tudo que estiver antes da ultima barra no artumento path
	Chamar os.path.basename(path) retornara uma strins contendo tudo que estiver apois a ultima barra no argumento path.
	Chamar os.path.split(path)	retornara uma tupla contendo essas duas strings, com o nome do diretorio e o nome base (caminho ate o diretorio atual e diretorio atual e ou arquivo)
'''

print(os.path.dirname('/home/yan/prog/python'))			#retornara uma string contendo tudo que estiver antes da ultima barra no artumento path
print(os.path.basename('/home/yan/prog/python'))		# uma strins contendo tudo que estiver apois a ultima barra no argumento path
print(os.path.split('/home/prog/python/workflow'))		#Se o nome de diretorio e o nome de base de um path forem necessarios ao mesmo tempo, chamar os.path.spli(path) para obter um valor de tupla contendo essas duas strings.

'''
	os.path.split(path) nao retorna uma lista de strings e sim somente uma tupla com caminho de diretorio e pasta atual
'''

calcFilePath = '/home/prog/python/workflow/calc.exe'
a = calcFilePath.split(os.path.sep)	#retorna uma lista de strings com o nome de cada pasta
print(a[1],a[3])


########################### Obtendo os tamanhos dos arquivos e o conteudo das pastas #########################################
'''
	Chamar os.path.getsize(path) 	retornara o tamanho em bytes do arquivo no argumento path.
	Chamar os.listdir(path)			retornara uma lista de strings com os nomes de arquivo para cada arquivo no argumento path
'''

t = os.getcwd()
v = os.path.getsize(t + '/files.py') * 8 / 1024 	#retornara o tamanho em Kbytes do arquivo no argumento path
print(v,'\n')
print(os.path.getsize(os.getcwd() + '/files.py') * 8 / 1024)	#'Pythonic' retornara o tamanho em Kbytes do arquivo no argumento path


print(os.listdir('/home/yan/prog'))		#retorna uma lista de strings com os nomes dos arquivos no diretorio passado como argumento



totalSize = 0
for filename in os.listdir('/home/yan/'):
	totalSize = totalSize + os.path.getsize(os.path.join('/home/yan/', filename))

print(totalSize)
'''
	Tamanho total da pasta.
	A medida que o loop percorre todos os nomes de arquivo da pasta a variavel totalSize é incrementada com o tamanho de cada arquivo.
'''



################################### Obtendo a validade de um path #########################################################
'''
	Chamar os.path.exists(path)		retornara True se o arquivo ou a pasta referenciada no argumento existir e False caso contrario.
	Chamar os.path.isfile(path)		retornara True se o argumento referente ao path existir e for um arquivo, retornara False caso contrario.
	Chamar os.path.isdir(path)		retornara True se o argumento referente ao path existir e for uma pasta e retornara False caso contrario.

'''

print(os.path.exists('/home'))	#verifica se o diretorio existe e retorna True caso sim, False caso contrario

print(os.path.isdir('/home'))	#verifica se o argumento passado é um diretorio e retorna True, se nao for retornara False.

print(os.path.isfile('/home/yan/prog/python/workflow/exerc.py'))	#verifica se o argumento passado é um arquivo e retorna True, caso não seja retorna False.
print(os.path.isfile('/home'))	


##################### Lendo arquivos #######################################################################
'''
	A chamada open() retorna um objeto File. Um objeto File representa um arquivo em seu computador. No exemplo armazenamos o objeto File na variavel helloFile.
	Agora, sempre que quisermos ler ou escrever no arquivo, poderemos fazer isso chamando os métodos do objeto File em helloFile.
	
	Se quisermos ler todo o conteudo de um arquivo como um valor de string, utilize o metodo read() do objeto File.
'''

helloFile = open('/home/yan/prog/python/workflow/helloFile.txt')
helloContent = helloFile.read()
print(helloContent)

'''
	Podemos utilizar o metodo readlines() para obter uma lista de valores de string para cada linha do arquivo
'''

helloFile = open('/home/yan/prog/python/workflow/helloFile.txt')
helloContent = helloFile.readlines()
print(helloContent)

########################################## Escrevendo em arquivos ##########################################
'''
	O Programa criara um arquivo chamado file.txt caso nao exista e chamar write() para escrever no arquivo.
	Ao abrir o file.txt novamente com argumento 'a', o programa ira adicionar texto ao arquivo.
'''
file = open('file.txt', 'w')
file.write('Holla que tal')			#abre e escreve
file.close()

file = open('file.txt')				#mostra o resultado dessa escrita
print(file.read())

file = open('file.txt', 'a')		#abre novamente e adiciona texto ao arquivo
file.write('\nmuy bien, i tu?')
file.close()

print('\nnew result: \/')			#mostra o novo resultado
file = open('file.txt')
print(file.read())



########################################## Salvando variaveis ##########################################
import shelve

'''
	Chame shelve.open() e passe um nome de arquivo, em seguida armazene o valor de shelf retornado em uma variavel.
	Voce pode fazer alteracoes no valor de shelf como se fosse um dicionario. Quando terminal chame close() no valor de shelf.
	Nesse caso, nosso valor de shelf esta armazenado em shelFile.
	Criamos uma lista cats e escrevemos em shelFile['cats'] = cats para armazenar a lista em shelFile como um valor associado a chave 'cats'
	(como em um dicionario)
'''
shelFile = shelve.open('mydata')
cats = ['name1', 'name2', 'name3']
shelFile['cats'] = cats

cats2 = ['name4', 'name5', 'name6']
shelFile['cats2'] = cats2

shelFile.close()



'''
	Os valores shelf nao precisam ser abertos em modo de leitura ou de escrita, amvas as operacoes serao permitidos apois os valores serem abertos
'''
shelFile = shelve.open('mydata')	#abre o arquivo onde foram gravados
print(shelFile['cats2'])			#exibe os resultados do dicionario na chave 'cats2'
print(shelFile['cats'])				##exibe os resultados do dicionario na chave 'cats'
shelFile.close()



'''
	Assim como os dicionarios, os valores de shelf tem metodos keys() e values() que retornarao as chaves e os valores do shelf em formatos semelhantes a listas.
'''shelFile = shelve.open('mydata')
print(list(shelFile.keys()))	#lista as chaves existentes no dicionario
print(list(shelFile.values()))	#lista os valores que estao dentro das chaves do dicionario
shelFile.close()



###################### Falta estudar o modulo pprint ##########################################################