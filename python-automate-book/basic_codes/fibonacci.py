def fibonacci(n):
    a,b = 0,1
    print a
    while (b < n):
        c = a
        a = b
        b = a + c
        print a

fibonacci(50)

'''
Debugging

c = 0
a = 1
b = 1+0

c = 1
a = 1
b = 1+1

c = 1
a = 2
b = 2+1

c = 2
a = 3
b = 3+2


0, -- 1,1,3,5
'''
