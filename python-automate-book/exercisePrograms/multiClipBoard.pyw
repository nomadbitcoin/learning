#!/usr/bin/env python3
#mcb.pyw - Salva e carrega porções de texto no clipboard.
#Usage: py.exe mcb.pyw save <palavra-chave> - Salva clipboard na palavra-chave.
#py.exe mcb.pyw <palavra-chave> - Carrega palavra chave no clipboard.
#py.exe mcb.pyw list - Carrega toda as palavras-chave no clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

#Salva conteudo no clipboard.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
#Lista palavras-chave e carrega conteudo
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])
	mcbShelf.close()