#!/usr/bin/env python3
import re
phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumberRegex.search('My number is 415-555-4242.')
print('Phone number found: '+ mo.group())
areaCode, mainNumber, otherNumber = mo.groups()
print(mo.group(1))
print(mo.group(2))
print(mo.group(3))
print(mo.group(0))
print(mo.groups())
print(areaCode)
print(mainNumber)
print(otherNumber)



#with parentesis
'''

phoneNumberRegex = re.compile(r'(\(\d\d\d\))(\d\d\d)-(\d\d\d\d)')
mo = phoneNumberRegex.search('My number is (415)555-4242.')

'''