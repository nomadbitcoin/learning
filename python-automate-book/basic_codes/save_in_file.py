my_name = raw_input('Please enter your name: ')
file = open('name', mode='w')
file.write(my_name)
file.close()

#file = open('name', mode='r')
#file.read()
