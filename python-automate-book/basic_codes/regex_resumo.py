? - corresponde a zero ou uma ocorrencia do grupo anterior
* -	corresponde a zero ou mais ocorrencias do gruo anterior
+ - corresponde a uma ou mais ocorrencias do grupo anterior
{n} - corresponde a exatamente n ocorrencias do grupo anterior
{n,} - corresponde a n ou mais ocorrencias do grupo anterior
{,m} - corresponde a zero até m ocorrencias do grupo anterior
{n,m} - corresponde a no minimo n e no maximo m ocorrencias do grupo anterior
{n,m}? ou *? ou +?  - faz uma correspondencia nongreedy do grupo anterior
^spam quer dizer que a string deve começar com spam
spam$ quer dizer que a string deve terminar com spam
. corresponde a qualquer caractere, exceto os caracteres de quebra de linha
''' \d,\w e \s correspondem a um digito, um caractere de palavra ou um caractere de espaço, respectivamente.
\D, \W e \S correspondem a qualquer caractere, exceto um digito, um caractere de palavra ou um caractere de espaço, respectivamente.
'''
[abc] corresponde a qualquer caractere que estiver entre os colchetes (por exemplo: a,b ou c) 