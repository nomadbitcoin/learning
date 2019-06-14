# Given the variables s and t defined as:
s = 'udacity'
t = 'bodacious'
# write Python code that prints out udacious
# without using any quote characters in
# your code.

temp = t.find('o')
temp1 = t.find('o',temp+1)

temp2 = t.find('i')
temp3 = t.find('s')
temp = s[:temp2]+t[temp1:temp3+1]

print temp
