spam = [['cat','bat'],[10,20,30]]
print(spam[1][-3])

spam = [['cat','bat','rat','elephant'],[10,20,30]]
print(spam[0][1:2])

spam = [['cat','bat','rat','elephant'],[10,200000000,30]]
print(len(str(spam[1][1])))

spam = [1,2,3]
spam = spam + ['a','b','c']
print(spam)

spam = ['cat','dog','rat','elephant']
del spam[2]
print(spam)