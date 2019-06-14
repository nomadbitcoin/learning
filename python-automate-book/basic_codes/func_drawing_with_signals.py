a = '+'
b = '-'
c = '|'
d = ' '

def func_temp_1():
    print a,(b+d)*4,a,(b+d)*4,a

def func_temp():
    temp=c+d*10
    temp1=temp+temp+c
    print(temp1)
    print(temp1)
    print(temp1)

def func_desenho():
    func_temp_1()
    func_temp()
    func_temp_1()
    func_temp()
    func_temp_1()

print func_desenho()
