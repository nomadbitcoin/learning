#!/usr/bin/env python3
#mapIt.py - incia o mapa no navegador usando um endereço da linha de comando ou clipboard.
import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
	#obtem o endereço da linha de comando 
	adress = ''.join(sys.argv[1:])		#a variavel sys.argv armazena uma lista contendo o nome de arquivo do programa e os argumentos de linha de comando. Se essa lista contiver mais informações além do nome do arquivo, len(sys.argv) será avaliado como um inteiro maior do que 1, o que quer dizer que argumentos de linha de comando foram fornecidos.
										#join transforma tudo em uma lista de string, passando [1:] ele desconsidera o primeiro valor de string pois nao queremos lidar com o nome do programa que foi passado como primeira string e o argumento como segunda string na linha de comando
else:
#obtém o endereço do clipboard.
	adress = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + adress)