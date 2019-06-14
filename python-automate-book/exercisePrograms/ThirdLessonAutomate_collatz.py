def collatz(number):
	if number % 2 == 0:
		print('your number // 2 is: ', end='')
		return number // 2
	else:
		print('3 * your number plus one is: ', end='')
		return 3 * number + 1
number = int(input('type a number '))
for i in range(number,1,-1):
	print(collatz(i))