def spam(divideBy):				
	try:							#Quando um codigo na clausula try causar um erro ele pulará para a clausula except
		return 42 / divideBy		#após executar esse código o programa contiuara normalmente
	except ZeroDivisionError:
		print('Error: Invalid argument.')
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

'''
def spam(divideBy):
	return 42 / divideBy

try:
	print(spam(2))
	print(spam(12))
	print(spam(0))			#depois de encontrar o erro o programa pula para except e continua dali em diante
	print(spam(1))
except ZeroDivisionError:
	print('Error: invalid argument.')

'''