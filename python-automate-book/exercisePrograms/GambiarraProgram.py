spam = ['apples','bananas','tofu','cats']
def newList(lista):
	a = len(lista)
	for i in range(0,a):
		lista[i]+= ','
		if i == a-1:
			lista.insert(-1,'and')
spam.append('batata')
print(newList(spam))

