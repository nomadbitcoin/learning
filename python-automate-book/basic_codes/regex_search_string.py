#!/usr/bin/env python3
import re
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search('My number is 415-555-4242.')
print('Phone number found: '+ mo.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())