#!/usr/bin/env python3
#bulletPointAdder.py adds wikipedia makrs it start

import pyperclip
text = pyperclip.paste()

#separate the lines and add asterisk.
lines = text.split('\n')
for i in range(len(lines)): #scroll throught all indexes on the list in loop
	lines[i] = '*' + lines[i] # add asterisk in each string on the list "lines"
	text = '\n'.join(lines)
pyperclip.copy(text)