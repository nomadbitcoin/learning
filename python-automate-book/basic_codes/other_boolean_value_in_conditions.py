name = ''
while not name:	#empty string considered a False boolean value -> not false = True, go to loop
	print('enter your name')
	name = input()
print('How many guests will you have')
numOfGuests = int(input())
if numOfGuests:
	print('Be sure to have enought room for all your guests')
print('Done')

#quando usados em condições 0, 0.0, ''(string vazia) são considerados False enquanto os demais valores são considerados True

#when used in conditions 0, 0.0 ''(empty string) are considered False while the other values are considered True