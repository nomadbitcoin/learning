#!/usr/bin/env python3
import re
greedyHaRegex = re.compile(r'(Ha){3,5}')
movv = greedyHaRegex.search('HaHaHaHaHa')
print(movv.group())

nonGreedyHaRegex = re.compile(r'(Ha){3,5}?')	#ponto de interrogação pode ter dois significados: declarar uma ocorrencia nongreedy ou indicar um grupo opcional
movv1 = nonGreedyHaRegex.search('HaHaHaHaHa')
print(movv1.group())


beginsWithHello = re.compile(r'^Hello')	#começa com uma string 'Hello'
print(beginsWithHello.search('Hello word!'))
print(beginsWithHello.search('He said hello.!')== None)

print('\n\n')

endWithNumber = re.compile(r'\d$')
print(endWithNumber.search('You number is 42'))  #termina com um numero

print('\n\n')

wholeStringsIsNum = re.compile(r'^\d+$')
print(wholeStringsIsNum.search('1234567890'))	#começa ou termina com um ou mais numeros {isso nao fez sentido no resultado que apresenta}
print(wholeStringsIsNum.search('12345a67890')== None)

atRegex = re.compile(r'.at')	#qualquer caractere
print(atRegex.findall('The cat in the rat sat on the flat mat.'))

nameRegex = re.compile(r'First Name:(.*) Last Name: (.*)')	#todo e qualquer caractere que venha depois de First Name e depois de Last Name
mo = nameRegex.search('First Name: AI Last Name: Sweigart') 	#o asterisco quer dizer `0 ou mais ocorrencias do caractere anterior`
print(mo.group())

nonGreedyRegex = re.compile(r'<.*?>')
mo1 = nonGreedyRegex.search('<To serve man> for dinner.>')
print(mo1.group())

nonGreedyRegex2 = re.compile(r'<.*>')
mo2 = nonGreedyRegex2.search('<To serve man> for dinner.>')
print(mo2.group())