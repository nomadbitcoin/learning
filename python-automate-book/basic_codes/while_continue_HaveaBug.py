while True:
	print('Who are you?')
	name = input()
	if name != 'Joe':
		continue			#Se a condição do if for True o continue reinicia o loop e se for False ele continua a instrução seguinte dentro do loop
		print('Hello, Joe. Whats is the password?(it is a fish.)')
		password = input()
		if password == 'swordfish':
			break
print('acess granted.')