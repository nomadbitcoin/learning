#! /usr/bin/python3.
# pw.py - a password repository program that is not secure 
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6','blog': 'VmALvQyKAxiVH5G8v01ifMLZF3sdt','luggage': 12345}
import sys, pyperclip
if len(sys.argv) < 2:
	print('Usage: python pw.py [account] - copy account password')
	sys.exit()
account = sys.argv[1] # the first argument in command line is the account

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('password for ' + account + ' copied to clipboard.')
else:
	print('There is no account named ' + account)