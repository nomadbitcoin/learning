Resumo:
		As listas e os dicionarios são valores que podem conter diversos valores, incluindo outras listas e outros dicionarios.
		Os dicionarios são úteis porque podemos mapear um item (a chave) a outro (o valor), diferente das listas que simplesmente contêm uma série de valores ordenados.
		Os valores em um dicionário são acessados por meio de colchetes, assim como nas listas.
		Em vez de um índice inteiro, os dicionários podem ter chaves que sejam de uma variedade de tipos de dados: inteiros, números de ponto flutuante, strings ou tuplas.
		Ao organizar os valores de um programa em estruturas de dados, podemos criar representações de objetos do mundo real. Vimos um exemplo disso com um tabuleiro de jogo da velha.
				


'''
    Os dicionarios podem usar varios tipos de dados diferentes, e nao apenas inteiros.
    Os indicies dos dicionarios sao chamados de chaves(keys), e uma chave juntamente com seu valor associado é chamado par chave-valor (key-value pair)
    Dicionarios sao criados usando chaves {}
'''

myCat = {'size':'fat','color':'gray','disposition':'loud'}

Isso atribui um dicionario a variavel myCat. As chaves desse dicionario sao 'size', 'color', 'disposition'. Os valores dessas chaves sao 'fat', 'gray', e 'loud'
Respectivamente esses valores podem ser acessados por meio de suas chaves

print(myCat['size']) 
-> a saida sera: 'fat'

print('My cat has ' + myCat['color'] + 'fur.')
-> a saida sera 'My cat has gray fur.'

-------------------------------------------------------------


'''
    De modo diferente das listas, os itens de um dicionario nao estao ordenados.
    O primeiro item de uma lista chamada spam sera spam[0]. Entretando ha "primeiro" item em um dicionario.
    Enquanto a ordem dos itens é importando para determinar se duas listas sao iguais, não importa em que ordem os pares chave-valor sao digitados em um dicionario.
'''

spam = ['cats','dogs','moose']
bacon = ['dogs','moose','cats']
print(spam == bacon)
-> saida sera: False

eggs = {'name':'Zophie','species':'cat','age':'8'}
ham = {'species':'cat','age':'8','name':'Zophie'}
print(eggs == ham)
-> saida sera: True

----------------------------------------------------

'''
    Ha tres metodos de dicionario que retornam valores semelhantes a listas contendo chaves, os valores ou amos - ou seja, as chaves e os valores - dicionario:
    keys(), values() e items(). Os valores retornados por esses metodos nao sao listas de verdade: eles nao podem ser modificados e nao tem um metodo append().
    Porem esses tipos de dados (dict_keys, dict_values e dict_items, respectivamente) podem ser usados em loops for
'''
spam = {'color':'red','age':42}
for v in spam.values():
    print(v)

-> saida sera: red, 42

Nesse caso, um loop for faz uma iteracao, percorrendo cada um dos valores do dicionario spam. Um loopfor pode fazer a iteracao passando pelas chaves ou pelas chaves e pelos valores:

for k in spam.keys():
    print(k)

-> saida sera: color, age

------------------------------------------------------------------------

Os valores no valor dict_items retornado pelo metodo items() sao tuplas contendo a chave e o valor.

spam = {'color':'red','age':42}
print(spam.items())

-> saida sera: '''dict_items([('color', 'red'), ('age', 42)])'''

-----------------------------------------------------------------------------------
'''
Podemos tambem utilizar o truque da atribuicao multipla em um loop for para atribuir a chave e o valor a variaveis diferentes.
'''
spam = {'color':'red','age':42}
for k,v in spam.items():
	print('Key: ' + k + ' Value: ' + str(v))

-> saida sera: Key: ageValue: 42, Key: colorValue: red

-------------------- Verificando se uma chave ou um valor estao presentes em um dicionario --------------------------------------------------------------

Os operadores in e not in podem verificar se um valor esta presente em uma lista e tambem em um dicionario.

spam = {'name':'Zophie','age':7}
print('name' in spam.keys())
-> saida sera True

spam = {'name':'Zophie','age':7}
print('Zophie' in spam.values())
-> saida sera True

spam = {'name':'Zophie','age':7}
print('color' in spam.values())
-> saida sera True

spam = {'name':'Zophie','age':7}
print('color' not in spam.values())
-> saida sera True


--------------------------------------------- Metodo get() ----------------------------------------------------

O metodo get() aceita dois argumentos: a chave do valor a ser obtido e um valor alternativo a ser retornado se essa chave nao existir.

picnicItems = {'appes':5, 'cups':2}
print('I am briging ' + str(picnicItems.get('cups',0)) + ' cups.')
print('I am briging ' + str(picnicItems.get('eggs',0)) + ' eggs.')

'''
    Como nao ha nenhuma chave 'eggs' no dicionario picnicItems, o valor default 0 é retornado pelo metodo get().
'''


---------------------------------------------- Metodo setdefault()---------------------------------------------------

Para definir um valor em um dicionario para uma chave especifica somente se essa chave ainda nao tiver um valor.
O primeiro argumento passado para o metodo setdefault() é a chave a ser verificada e o segundo é o valor a ser definido nessa chave caso ela não exista.
Se a chave existir, o método setdefault() retornará o valor da chave.


spam = {'name': 'Pooka', 'age':5}
print(spam.setdefault('color','black')) #retorna o valor 'black' pois esse agora é o valor definido para a chave 'color'.
print(spam.setdefault('color','white')) 

''' Quando spam.setdefault('color','white') é chamado a seguir, o valor dessa chave não é alterado para 'white', pois spam ja tem uma chave de nome 'color'
'''

--------------------------------------------------------------------------------------------------------------------


################################# Programs #############################
'''
	Suponha que voce queira que seu programa armazene dados relativos as datas de aniversario de seus amigos.
	Podemos usar um dicionario com os nomes como chaves e as datas de aniversario como valores.
'''

birthdays = {'Alice':'Apr 1','Bob':'Dec 12', 'Carol':'Mar 4'}
while True:
	print('Enter a name: (blank to quit)')
	name = input()
	if name == "":
		break
	if name in birthdays:
		print(birthdays[name] + ' is the birthday of ' + name)
	else:
		print('I do not have birthday information for ' + name)
		print('What is their birthday?')
		bday = input()
		birthdays[name] = bday
		print('Birthday database updated.')

######################################################################
######################################################################		Programa que conta o numero que os caracteres aparecem em uma string, e faz uma apresentacao elegante
######################################################################

''' Um programa que conta o numero de ocorrencias de cada letra em uma string.
'''
import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1

pprint.pprint(count)

''' O programa percorre todos os caracteres da string contida na variavel message em um loop, contabilizando cada caractere presente.
    A chamada ao metodo setdefault() garante que a chave esta no dicionario count (com um valor default igual a 0) para que o programa nao lance um erro KeyError quando count[character] = count[character] +1 for executado.
'''


######################################################################
######################################################################		Conta quantos itens cada um levou para p picnic
#######################################################################

allguests = {'Alice':{'apples':5,'pretzels':12}, 
'Bob':{'ham sandwiches':3, 'apples':2},
'Carol':{'cups':3, 'apple pies:':1}}

def totalBrought(guests, item):
    numBrought = 0
    for k,v in allguests.items():
        numBrought = numBrought + v.get(item,0)
    return numBrought

print('Number of things being brought:')
print('- Apples     ' + str(totalBrought(allguests,'apples')))
print('- Cups     ' + str(totalBrought(allguests,'cups')))
print('- Cakes     ' + str(totalBrought(allguests,'cakes')))
print('- Ham Sandwiches     ' + str(totalBrought(allguests,'ham sandwiches')))
print('- Apple Pies     ' + str(totalBrought(allguests,'apple pies')))