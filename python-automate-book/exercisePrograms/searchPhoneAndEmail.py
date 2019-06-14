#!/usr/bin/env python3
#find phone and mail adress in the clipboard.
import pyperclip, re

phoneRegex = re.compile(r'(\d{3}|\(\d{3}\))?(\s|-|\.)(\d{3})(\s|-|\.)(\d{4})(\s*(ext|x|ext.)\s*(\d{2,5})?)')

#ALL: create a regex to search mail
emailRegex = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4})')

#ALL: find correspondences on the text in clipboard
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1], groups[2], groups[3], groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)
for groups in emailRegex.findall(text):
	matches.append(groups[0])


#ALL: copy results to clipboard
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard:')
	print('\n'.join(matches))
else:
	print('No phone numbers or email addresses found.')


'''
Copied to clipboard:
800-420-7240
415-863-990
415-863-9950
info@nostarch.com
media@nostarch.com
academic@nostarch.com
help@nostarch.com

'''