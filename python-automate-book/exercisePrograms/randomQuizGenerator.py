#!/usr/bin/python3
#create quizzes with questions and answers in random order, along with the templates containing the answers 
import random
#os dados para as provas. As chaves sao os estados e os valores sao as capitais
capitals = {'Rio Grande do Sul': 'Porto Alegre','Santa Catarina': 'Florianopolis','Parana': 'Curitiba','Sao Paulo': 'Sao Paulo',
			'Rio de Janeiro': 'Rio de Janeiro', 'Espirito Santo': 'Vitoria', 'Bahia': 'Salvador', 'Mato Grosso': 'Cuiaba', 
			'Minas Gerais': 'Belo Horizonte','Acre': 'Rio Branco', 'Alagoas': 'Maceio', 'Amapa': 'Macapa', 'Amazonas': 'Manaus',
			'Ceara': 'Fortaleza', 'Distrito Federal': 'Brasilia', 'Goias': 'Goiania', 'Maranhao': 'Sao Luis', 'Mato Grosso do Sul': 'Campo Grande',
			'Para': 'Belem', 'Paraiba': 'Joao Pessoa', 'Pernambuco': 'Recife', 'Piaui': 'Teresina', 'Rio Grande do Norte': 'Natal', 'Rondonia': 'Porto Velho',
			'Roraima': 'Boa Vista', 'Sergipe': 'Aracaju', 'Tocantins': 'Palmas'}


#Gera 35 arquivos contendo as provas
for quizNum in range(35):
	#cria os arquivos com as provas e os gabaritos das respostas.
	quizFile = open('capitals%s.txt' % (quizNum + 1),'w')
	answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1),'w')


#Escreve o cabeçalho da prova.
quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
quizFile.write((' ' * 20)+ 'State Capitals Quiz (Form%s)' % (quizNum + 1))
quizFile.write('\n\n')


#Embaralha a ordem dos estados.
states = list(capitals.keys())
random.shuffle(states)


#Percorre todos os 50 estados em um loop, criando uma pergunta para cada um.
for questionNum in range(50):
	#Obtem as respostas corretas e incorretas.
	correctAnswer = capitals[states[questionNum]]
	wrongAnswers = list(capitals.values())
	del wrongAnswers[wrongAnswers.index(correctAnswer)]
	wrongAnswers = random.sample(wrongAnswers, 3)
	answerOptions = wrongAnswers + [correctAnswer]
	random.shuffle(answerOptions)


#Grava a pergunta e as opcoes de resposta no arquivo de prova
quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
for i in range(4):
	quizFile.write('	%s. %s\n' % ('ABCD'[i], answerOption[i]))
	quizFile.write('\n')


#Grava o gabarito com as respostas em um arquivo.
answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOption.index(correctAnswer)]))
quizFile.close()
answerKeyFile.close()