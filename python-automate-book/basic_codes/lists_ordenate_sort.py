spam = [2,5,3.14,1,-7]
spam.sort()
print(spam)

spam = ['ants','cats','dogs','badgers','elephants']
spam.sort()
print(spam)

spam = ['ants','cats','dogs','badgers','elephants']
spam.sort(reverse=True)
print(spam)

spam = ['A','a','Z','z']
spam.sort(key=str.lower)
print(spam)