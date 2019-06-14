#!/usr/bin/env python3
import re
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food. BABY FOOD'))

#[a-zA-Z0-9]
#[0-5.] será de 0 até 5 com um ponto no final

consoantRegex = re.compile(r'[^aeiouAEIOU]')
print(consoantRegex.findall('Robocop eats baby food. BABY FOOD'))



