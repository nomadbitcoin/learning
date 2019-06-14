#!/usr/bin/python3

'''
	tabela caracteres regex

	\d -> qualquer caractere que seja um numero
	\D -> qualquer caractere que nao seja um numero
	\w -> qualquer letra, digito ou caractere underscore (underline)
	\W -> qualquer caractere que nao seja, digito, letra ou underscore 
	\s -> quaquer espaco, quebra de linha ou tabulacao
	\S -> qualquer caractere que nao seja um espaco, uma tabulacao ou uma quebra de linha.

'''
'''
	| -> corresponder a mais de uma opcao como: 'Bat(|man|car|movel)'correspondera a Batman ou a Batcar ou a Batmovel.
	+ -> corresponde a uma ou mais ocorrencias como: 'Bat(wo)+man' correspondera a Batwoman ou Batwowowowoman mas nao a Batman.
	* -> corresponder a zero ou mais ocorrencias como: 'Bat(wo)*man' ira corresponder a Batman ou a Batwoman.
	? -> correspondencia opcional como: 'Bat(wo)?' ira corresponder a Batman ou Batwoman mas nao a Batwowoman.
	'(\d)' -> grupo de digitos.
'''
'''
	'[0-5]' -> qualquer digito de 0 ha 5
	'{3}' -> corresponder a tres vezes a string de um grupo de caracteres.
	'{3,}' -> corresponder a 3 ou mais vezes.
	'{,5}' -> corresponde de zero a cinco vezes a string.	
	'{3,5}' -> de 3 a 5 correspondencias de um grupo especifico de caracteres
		mood default = greedy = ira corresponder ao maior string que encontrar: ex '(Ha){3,5}' ira corresponder a HaHaHaHaHa (5xHa) e nao a menor delas (3xHa)
		modo non-greedy acrescenda interrogacao ? =  ira corresponder a menos delas, nesse caso: 3 vezes Ha (HaHaHa)
'''
'''		Nos colchetes os simbolos normais de expressoes regulares nao sao interpretados
	[aeiouAEIOU] -> Correspondera a qualquer vogal tanto minuscula ou maiuscula.
	[^aeiouAEIOU]') usar o caractere (^) correspondera a tudo que nao estiver na classe seguinte, nesse caso, todas as consoantes
	[0-5.] -> correspondera aos caracteres de 0 a 5 e um ponto
	[a-zA-Z0-9] -> correspondera a todos os caracteres minusculos ou maiusculos de a ate z e aos digitos de 0 ate 9

'''
'''
	endsWithNumber = re.compile(r'\d$')     #corresponde a strings que terminem com um numero
	startsWithEndsWith = re.compile(r'^\d$')    #corresponde a strings que comecem e terminem com um numero
	begginsWithHello = re.compile(r'^Hello') #corresponde a strings que comece com Hello
'''
'''
	Ponto quer dizer qualquer caractere e asterisco zero ou mais vezes (exceto quebra de linha)
	(r'<.*?>')   #ira pegar <text text>
	(r'<.*?>')   #ira pegar <text text>
	(r'<.*>', re.DOTALL)   #correspondera a regex inclusive a quebras de linha
'''
'''
	namesRegex = re.compile(r'Agent \w+')
	namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
	saida sera: CENSORED gave the secret documents to CENSORED.
	
	agentNamesRegex = re.compile(r'Agent (\w)\w*')
	agentNamesRegex.sub(r'\1***', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
	saida sera: A**** told C**** that E**** knew Bob was a double agent
'''
''' 
	#Podemos distribuir a expressao regular em varias linhas usando comentarios como e re.VERBOSE como segundo argumento:
	phoneRegex = re.compile(r'''(
		(\d{3}|(\d{3}\))?      #codigo de area
		(\s|-|\.)               #separador
		(\d{3})                 #primeiros tres digitos
		(\s|-|\.)               #separador
		\d{4})                  #ultimos 4 digitos
		(\s*(ext|x|ext.)\s*\d{2,5})?    #extensao
	)''',re.VERBOSE)
'''
'''	#Combinando re.IGNORECASE, re.DOTALL e re.VERBOSE
	someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
'''



############################ Encontrando numeros de telefone em um arquivo de texto	#################################################################
import re

'''
	Passar um valor de string que represente sua expressao regular a re.compile() fara um objeto Regex 
	de padrao ser retornado(ou, simplesmente, um objeto Regex).
	a variavel phoneNumRegex contem um objeto Regex
'''
phoneNumRegex = re.compile(r'\d\d\d\d\d\d\d\d\d\d|\d\d-\d\d\d\d-\d\d\d\d|\d\d\d-\d\d\d-\d\d\d|\d\d-\d\d\d\d\d-\d\d\d\d')

#open file with contact numbers
file = open('contacts.txt')
textReaded = file.readlines()

t = 0
for phoneFounded in range(len(textReaded)):	
	'''
		o metodo search() de um objeto regex pesquisa a string recebida em busca de qualquer correspondencia com a regex. Retornara None se o padrao nao for encontrado na string.
		Se for encontrado, o metodo search() retornara um objeto Match. Objetos Match tem um metodo group() que retornara o texto correspondente extraido da string pesquisada.
	'''
	objectMatch = phoneNumRegex.search(textReaded[phoneFounded])
	if objectMatch == None:
		continue
		#contador para dizer quantos numeros encontrou
		t = t+1
		print(str(t) + ' Phone number found: ' + objectMatch.group())



############################################ expressoes regulares com grupos #######################################
'''
	Usar parenteses separa em grupos e usando a funcao print com group(1) ira mostrar apenas o grupo em questao
	usar groups() no plural ira retornar todos os grupos
	usar group(0) ira retornar o que encontrou
'''
import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')

mo = phoneNumRegex.search('My number is 415-555-4242')

print(mo.group(0))
print(mo.groups())




####################################### Mais de uma correspondencia #################################3
'''
	o Pipe |, pode ser usado para fazer correspondencia de um entre diversos padroes como parte de sua regex
	Por exemplo, suponha que voce queira fazer a correspondencia de qualquer uma das strings:
	'Batman', 'Batmobile', 'Batcopter', 'Batbat'. como todas essas strings comecam com bat, seria interessante se voce pudesse especificar esse prefixo somente uma vez, isso pode ser feito com paranteses.
'''
import re
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile losta a wheel')
print(mo.group())
'''
	A chamada ao metodo mo.group() retorna o texto correspondente 'Batmobile' completo, enquanto mo.group(1) retorna somente a parte do texto correspondente. No caso, 'mobile'
'''

####################################### Correspondencia opcional  com ponto de interrogacao #################################

import re
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman, and Batwoman')
print(mo.group())

'''	A parte da expressao regular que contem (wo)? significa que o padrao wo é opcional.
	A regex correspondera a textos que nao tenham nenhuma ou que tenham uma instancia de wo.
	Por isso a regex corresponde tanto a Batwoman quanto a Batman.
'''

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

-------------------------------------------------------------
-------------------------------------------------------------
-------------------------------------------------------------

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')

mo1 = phoneRegex.search('My number is 415-555-4242')

mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())
'''	Voce pode pensar no ? como se dissesse "faca a correspondencia de zero ou de uma ocorrencia de grupo que antecede esse ponto de interrogacao"
print(mo1.group())
'''



####################################### Correspondendo a zero ou mais com asterisco #################################

'''	O * (asterisco) quer dizer "corresponda a zero ou mais" - o grupo que antecede o asterisco pode ocorrer qualquer numero de vezes no texto.
	Esse grupo podera estar totalmente ausente ou ser repetido diversas vezes.
'''
import re
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())


mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())


mo3 = batRegex.search('The Adventures of Batwowowoman')
print(mo3.group())


####################################### Correspondendo a uma ou mais com sinal de adicao #################################

'''	O sinal de + (adicao) quer dizer "corresponda a uma ou mais"
	O grupo que antecede ao sinal de + deve aparecer pelo menos uma vez.
'''
import re
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())


mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())


mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None)



####################################### Correspondendo a repeticoes especificas usando chaves #################################

'''Se tiver um grupo que deseja repetir um umero especifico de vezes, insira um numero entre chaves apos o grupo em sua regex
	a regex (Ha){3} corresponde a string HaHaHa, mas nao a HaHa pois essa ultima tem duas repeticoes apenas.
Em vez de um numero, podemos especificar um intervalo especificando um minimo  e um maximo
	(Ha){3,5} corresponde a HaHaHa, HaHaHaHa e HaHaHaHaHa
'''

Tambem podemos deixar de fora o primeiro ou o segundo numero nas chaves para deixar de especificar o minimo ou o maiximo
(Ha){3,} correspondera a tres ou mais instancias do grupo (Ha)
(Ha){,5} correspondera a zero ate cinco instancias

import re
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())

print((haRegex.search('Ha') == None))


####################################### Correspondencias greedy e non greedy ####################################################

'''As expressoes regulasres em python são gulosas por padrão, ou seja, sempre corresponderao ao maior string possivel.
	Como em {3,5} ela correspondera a HaHaHaHaHa mesmo que tenham HaHaHa ou HaHaHaHa.

	Na versao nonGreedy basta digitar um ponto de interrogacao apos a chave de fechamento.

'''
import re
greedyRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyRegex.search('HaHaHaHaHa')		#ira pegar a primeira correspondencia, ou seja, HaHaHa

print(mo1.group())

'''	Observe que os pontos de interrogacao podem ter dois significados em expressoes regulares, declarar uma correspondencia non Greedy 
ou indicar um grupo opcional, esses significados nao tem nenhuma relacao entre si.
'''

####################################### Metodo findall() #######################################

''' Alem do metodo search(), os objetos regex tambem tem um metodo findall() 
que retorna as strings de todas as correspondencias na string pesquisasda.
	Funciona somente se nao tiver grupos
'''
import re

phoneRegexNum = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo1 = phoneRegexNum.findall('Cell: 415-555-9999 Work: 212-555-0000')    #nao tem grupos
print(mo1)
a saida eh: ['415-555-9999', '212-555-0000']		#lista de strings

#################################	Encontra numeros de telefone em arquivo #########################

import re

phoneNumRegex = re.compile(r'\d\d\d\d\d\d\d\d\d\d|\d\d-\d\d\d\d-\d\d\d\d|\d\d\d-\d\d\d-\d\d\d|\d\d-\d\d\d\d\d-\d\d\d\d')

#open file with contact numbers
file = open('contacts.txt')
textReaded = file.read()

print(phoneNumRegex.findall(textReaded))

##################################################################	

''' Se ouver grupos na expressao regular , findall retornara uma lista de tuplas. Cada tupla retornara uma correspondencia identificada
e seus intens serao strings correspondentes a cada grupo da regex

'''	

import re

phoneRegexNum = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')     #tem grupos
mo1 = phoneRegexNum.findall('Cell: 415-555-9999 Work: 212-555-0000')  
print(mo1)
a saida eh: [('415', '555', '9999'), ('212', '555', '0000')]		#tuplas

##################################################################	Correspondendo a underline e outros caracteres ao mesmo tempo
import re

xmaxRegex = re.compile(r'\d+\s\w+')

print(xmaxRegex.findall('12 drummers_, 11 pipers, 10 lords, 9 ladies'))




################################################ Caracteres Especiais ################################################ 
'''	[aeiouAEIOU] Correspondera a qualquer vogal tanto minuscula ou maiuscula
'''


import re
vogelRegex = re.compile(r'[aeiouAEIOU]')
print(vogelRegex.findall('Robocop eats baby food. BABY FOOD'))


saida sera: ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']

#################################################################
'''	[^aeiouAEIOU]') usar o caractere (^) correspondera a tudo que nao estiver na classe seguinte, nesse caso, todas as consoantes
'''

import re
vogelRegex = re.compile(r'[^aeiouAEIOU]')
print(vogelRegex.findall('Robocop eats baby food. BABY FOOD'))

saida sera: ['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D']

################################################################# Usando circunflexo e simbolo de dolar #################################################################

import re
'''
    O simbolo de acento circunflexo ^ tambem pode ser usado no inixio de uma regex para indicar que uma correspondencia deve ocorrer no inicio de um texto pesquisado.
    Da mesma maneira podemos colocar o simbolo do dolar $ no final de uma regex para indicar que a string deve terminal com esse padrao de regex. 
    Alem disso podemos combinar ^ com $ juntos para indicar que a string toda deve corresponder a regex.
'''

begginsWithHello = re.compile(r'^Hello')	#a string deve comear com Hello
ba = begginsWithHello.search('Abacate Hello world!')
print(ba.group()) #retornara None pois nao comeca com Hello e sim com Abacate

endsWithNumber = re.compile(r'\d$')     #corresponde a strings que terminem com um numero

startsWithEndsWith = re.compile(r'^\d$')    #corresponde a strings que comecem e terminem



################################################################# Caractere Curinga
import re

'''	o caractere . (ponto) em uma expressao regular eh chamado de caractere curinga, corresponde a qualquer caractere exceto uma quebra de linha
'''

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))       #qualquer caractere que esteja antes de at

saida sera: ['cat', 'hat', 'sat', 'lat', 'mat']

################################################################# Correspondendo a tudo usando o caractere ponto-asterisco
'''
	Ponto quer dizer qualquer caractere e asterisco zero ou mais vezes (exceto quebra de linha)
'''

############################## Modo non greedy

import re

nonGreedyRegex = re.compile(r'<.*?>')   #ira pegar <text text>
mo = nonGreedyRegex.search('<text text> texto texto>')  
print(mo.group())

################################################################# Modo Greedy

import re

nonGreedyRegex2 = (r'<.*?>')   #ira pegar <text text>
mo = nonGreedyRegex2.search('<text text> texto texto>')  
print(mo.group())

################################################################# Pegando quebras de linha tambem


import re

nonGreedyRegex2 = re.compile(r'<.*>', re.DOTALL)   #correspondera a regex inclusive a quebras de linha
mo = nonGreedyRegex2.search('<text text\n texto texto>')  
print(mo.group())


################################################################# Substituindo Strings #################################################################

''' O metodo sub() dos objetos regex recebe dois argumentos. O primeiro uma string para substituir qualquer correspondencia.
    O segundo a string para a expressao regular..
    O metodo sub() retorna uma string com as substituicoes aplicadas.
'''
import re

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

saida sera: CENSORED gave the secret documents to CENSORED.

#################################################################

''' As vezes pode ser necessario utilizar o proprio texto correspondente como parte da substituicao.
    No primeiro argumento de sub() podemos digitar \1,\2,\3 e assim por diante para dizer
"insira o texto do grupo 1,2,3 e assim por diante na substituicao".
'''

import re
agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1***', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

saida sera: A**** told C**** that E**** knew Bob was a double agent.

################################################################# Administrando Regex Complexas 
Podemos distribuir a expressao regular em varias linhas usando comentarios como:


phoneRegex = re.compile(r'''(
    (\d{3}|(\d{3}\))?      #codigo de area
    (\s|-|\.)               #separador
    (\d{3})                 #primeiros tres digitos
    (\s|-|\.)               #separador
    \d{4})                  #ultimos 4 digitos
    (\s*(ext|x|ext.)\s*\d{2,5})?    #extensao
)''',re.VERBOSE)


################################################################# Combinando re.IGNORECASE, re.DOTALL e re.VERBOSE

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
