#!/usr/bin/env python3
import re

namesRegex = re.compile(r'Agent \w+')	#primeiro argumento de sub abaixo diz o texto que ira substituir o texto em questao passado no segundo argumento
print(namesRegex.sub('CENSORED','Agent Alice gave the secret documents to Agent Bob.'))

agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****','Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))