import os
n = []
a = ['not found','once','twice','three','four','five','times']

n.append('the life is good very good w.w.w.w.w')     #position [0] in n
print 'the text to you avaliate: ',n[0]
n.append(raw_input('\nType a text part do you want search in the avaliated text\n'))    #position [1] in n
n.append(n[0].count(n[1]))  #position [2] in n count how much times have found the word
os.system('clear')

if n[2] == 0:       #if not found the word
    print "Searched '",n[1],"' "' in the text  "',n[0],'"'
    print a[0]
elif n[2]>0:
    n.append(n[0].index(n[1])) #position [3] in n   #first position found the word
    if n[2] == 1:
        print 'the word was found',a[1]
    if n[2] == 2:
        n.append(n[0].index(n[1],n[3]+1))   #position [4] in n  #second position found the word
        print 'the word was found',a[2]
    if n[2] == 3:
        n.append(n[0].index(n[1],n[3]+1))   #position [4] in n #second position found the word
        n.append(n[0].index(n[1],n[4]+1))   #position [5] in n  #thirth position found the word
        print 'the word was found',a[3],a[-1]
    if n[2] == 4:
        n.append(n[0].index(n[1],n[3]+1))   #position [4] in n #secon\\d position found the word
        n.append(n[0].index(n[1],n[4]+1))   #position [5] in n  #thirth position found the word
        n.append(n[0].index(n[1],n[5]+1))   #position [6] in n  #fourth position found the word
        print 'the word was found',a[4],a[-1]
    if n[2] == 5:
        n.append(n[0].index(n[1],n[3]+1))   #position [4] in n #secon\\d position found the word
        n.append(n[0].index(n[1],n[4]+1))   #position [5] in n  #thirth position found the word
        n.append(n[0].index(n[1],n[5]+1))   #position [6] in n  #fourth position found the word
        n.append(n[0].index(n[1],n[6]+1))   #position [6] in n  #fiveth position found the word
        print 'the word was found',a[5],a[-1]
    print n
