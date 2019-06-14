import random
secretNumber = random.randint(1,20)
print('i am thinking of a number between 1 and 20.')

#peça para o jogador adivinhar 6 vezes.
for guessesTaken in range(1,7):
	print('Take a gress.')
	guess = int(input())
	if guess < secretNumber:
		print('You gress is to low.')
	elif guess > secretNumber:
		print('Your guess is to high.')
	else:
		break #esta condiçao corresponde ao palpite correto
if guess == secretNumber:
	print('Good job! you guesses my number in ' + str(guessesTaken) + ' guesses!')
else:
	print('Nope. The number I was thinking of was ' + str(secretNumber))