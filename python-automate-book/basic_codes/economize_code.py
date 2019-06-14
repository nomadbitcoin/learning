import random

def getAnswer(answerNumber):
	if answerNumber == 1:
		return 'it is certain - number one'
	elif answerNumber == 2:
		return 'number two'
	elif answerNumber == 3:
		return 'number three'
	elif answerNumber == 4:
		return 'number four'
	elif answerNumber == 5:
		return 'number five'
	elif answerNumber == 6:
		return 'number six'
	elif answerNumber == 7:
		return 'number seven'
	elif answerNumber == 8:
		return 'Number eight'
	elif answerNumber == 9:
		return 'Number nine'
	elif answerNumber == 0:
		return 'number zero'
	else:
		return 'sei nao ein'
#r = random.randint(1,9)
#fortune = getAnswer(r)
#print(fortune)

print(getAnswer(random.randint(1,9)))