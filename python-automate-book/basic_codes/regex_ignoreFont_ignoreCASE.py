#!/usr/bin/env python3
import re

robocop = re.compile(r'robocop',re.I)
print(robocop.search('RoboCop is part man, part machine, all cop').group())

print(robocop.search('ROBOCOP protects the innocent.').group())

print(robocop.search('AI, why dows your programming book talk about robocopp so much?').group())
