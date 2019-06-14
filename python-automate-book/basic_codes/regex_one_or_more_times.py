#!/usr/bin/env python3
import re
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group())

mo3 = batRegex.search('The adventures of Batwowowowoman')
print(mo3.group())

print('\n\n')

batRegex1 = re.compile(r'Bat(wo)+man')
vo = batRegex1.search('The adventures of Batwoman')
print(vo.group())

vo1 = batRegex1.search('The adventures of Batwowowowoman')
print(vo1.group())

vo2 = batRegex1.search('The adventures of Batman')
print(vo2 == None)

haRegex = re.compile(r'(Ha){3}')
to = haRegex.search('HaHaHa')
print(to.group())

to1 = haRegex.search('Ha')
print(to1 == None)