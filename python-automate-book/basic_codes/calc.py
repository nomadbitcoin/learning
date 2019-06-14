# coding=UTF-8
input_1 = raw_input('do you want to do an aritmetic operation? ')
if input_1 == 'yes':
    num_1 = input('write a first number : ')
    num_2 = input('write a second number : ')
    soma = num_1 + num_2
    import os
    os.system('clear')
    print 'the sum value is:',soma

if input_1 == 'no':
    print 'the other option is the concatenation of strings: '
    str_1 = raw_input('write a first word: ')
    str_2 = raw_input('write a second word: ')
    str_result = str_1 + str_2
    print 'the text became:', str_result
