def factorial(n):
    res = 1
    while n >= 1:
        res = res * n
        n = n - 1
    return res
print factorial(4)
print factorial(5)
print factorial(6)


#    n * (n-1) * n * (n-2) * n * (n-3)

#print factorial(4)
#>>> 24
#print factorial(5)
#>>> 120
#print factorial(6)
#>>> 720
