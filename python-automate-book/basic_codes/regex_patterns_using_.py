#!/usr/bin/env python3
import re
heroRegex =  re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

print('\n\n\n')


batRegex1 = re.compile(r'Bat(wo)?man')
moo1 = batRegex1.search('The adventures of Batman')
moo2 = batRegex1.search('The adventures of Batwoman')
print(moo1.group())
print(moo2.group())


phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d')
mow1 = phoneRegex.search('My number is 415-555-4242')
print(mow1.group())