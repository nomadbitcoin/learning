def spam():
	global eggs
	eggs = 'spam'	#essa variavel é global
def bacon():
	eggs = 'bacon'	#essa é uma variavel local
def ham():
	print(eggs)		#essa é uma variavel global
eggs = 42 		#essa é a variavel global
spam()
print(eggs)