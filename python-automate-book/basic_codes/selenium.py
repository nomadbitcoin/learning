***************************************************************
********* localizar elementos na pagina	***********************
***************************************************************

find_element_*   ->> os metodos find_element_ retornam um unico objeto WebElement que representa o primeiro elemento da pagina que corresponda a consulta


find_elements_*	 ->> os metodos find_elements_ retornam uma lista de objetos WebElement_* contendo todos os elementos correspondentes na pagina.


Tabela - Metodos WebDriver do selenium para encontrar elementos
-----------------------------------------------------------------------------------------
| browser.find_element_by_class_name(nome)			|  Elementos que utilizam a classe 	|
| browser.find_elements_by_class_name(nome)			|  CSS  nome.						|
-----------------------------------------------------------------------------------------
| browser.find_element_by_css_selector(seletor)		|	Elementos que correspondem		|
| browser.find_elements_by_css_selector(seletor)	|	ao seletor CSS.					|
-----------------------------------------------------------------------------------------
| browser.find_element_by_id(id)					|	Elementos com um 				|
| browser.find_elements_by_id(id)					|	valor de atributo id 			|
|													|	correspondente. 				|
|													|									|
| browser.find_element_by_link_text(texto)			|	Elementos <a>					|
| browser.find_elements_by_link_text(texto)			|	que correspondem				|
|													|	totalmente ao texto				|
|													|	especificado.					|
|													|									|
| browser.find_element_by_partial_link_text(texto)	|	Elementos <a> 					|
| browser.find_elements_by_partial_link_text(texto)	|	que contem o texto				|
|													|	especificado.					|
-----------------------------------------------------------------------------------------
| browser.find_element_by_name(nome) 				|	Elementos com um valor			|
| browser.find_elements_by_name(nome)				|	de atributo nome correspondente |
-----------------------------------------------------------------------------------------
| 													|	Elementos com uma tag nome		|
| browser.find_element_by_tag_name(nome)			|	correspondente (sem diferenciar)|
| browser.find_elements_by_tag_name(nome)			|	letras maiusculas de minusculas;|
| 													|	um elemento <a> correspondentes |
|													|	a 'a' e 'A'						|
-----------------------------------------------------------------------------------------
Exceto pelos metodos *_by_tag_name(), os argumentos para todos os metodos consideram diferencas
entre letras maiusculas e minusculas. Se nao houver nenhum elemento na pagina
que corresponda ao que o metodo esta procurando, o modulo selenium 
gerara uma excecao NoSuchElement (que devera ser acrescentada a um try para que o programa nao pare)

apos ter o objeto WebElement podera descobrir mais sobre ele ao ler os atributos ou chamar os metodos da tabela abaixo.

-------------------------------------------------------------------------------------------------------------------------------------
| tag_name 				| O nome da tag, por exemplo, 'a' para um elemento <a>.														|
-------------------------------------------------------------------------------------------------------------------------------------
| get_attribute(nome)	| O valor do atributo nome do elemento.																		|
-------------------------------------------------------------------------------------------------------------------------------------
| text 					| O texto do elemento, por exemplo, 'hello' em <span> hello </span>.										|
-------------------------------------------------------------------------------------------------------------------------------------
| clear()				| Para campos de texto ou elementos correspondentes a area de texto, limpa o texto digitado.				|
-------------------------------------------------------------------------------------------------------------------------------------
| is_displayed()		| Retorna True se o elemento estiver visivel; caso contrario, retorna False.								|
-------------------------------------------------------------------------------------------------------------------------------------
| is_enabled()			| Para elementos de entrada, retorna True se o elemento estiver habilitado; caso contrario, retorna False.	|
-------------------------------------------------------------------------------------------------------------------------------------
| is_selected()			| Para elementos relacionados a caixas de selecao ou botoes de radio, retorna True,							|
|						| se o elemento estiver selecionado; caso contrario, retorna False.											|
-------------------------------------------------------------------------------------------------------------------------------------
| location				| Um dicionario com chaves 'x' e 'y' para a posicao do elemento na pagina. 									|
-------------------------------------------------------------------------------------------------------------------------------------

#####################################

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
try:
	elem = browser.find_element_by_class_name('dropdown-menu')
	print('Found <%s> element with that class name!' % (elem.tag_name))
except:
	print('Was not able to find an element with that name.')

'''
	Nesse caso, abrimos o firefox e o direcionamos a um URL. Nessa pagina, tentamos encontrar
	elementos com nome de classe igual a 'dropdown-menu' e, caso esse elemento seja encontrado,
	exibimos seu nome de tag usando o atributo tag_name. Se um elemento desse tipo nao for encontrado,
	exibimos uma mensagem diferente.
'''

#####################################


**********************************************************************
**************************Clicando na pagina: ************************
**********************************************************************

Os objetos WebElement retornados pelos metodos find_element_* e find_elements_*
tem um metodo click() que simula um clique de mouse nesse elemento. Esse metodo
pode ser usado para seguir um link, fazer uma selecao em um botao de radio,
clicar em um botao Submit (Submeter) ou disparar qualquer evento que possa ocorrer
quando esse elemento for clicado pelo mouse.


from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Forum')
print(type(linkElem))

linkElem.click()	#segue o link "Forum"

'''
	Esses comandos abrem o Firefox em http://inventwithpython.com, obtem o objeto
	WebElement para o elemento <a> com o texto ~ Forum ~ e entao simulam um clique
	nesse elemento <a>. Como se voce mesmo tivesse clicado no link;

'''


*******************************************************************************
********************* Preenchendo e enviando Formularios **********************
*******************************************************************************

Enviar teclas aos campos de texto em uma pagina web é uma questao de encontrar
o elemento <input> ou <textarea> para esse campo de texto e chamar o metodo
send_keys(). 


from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://mail.yahoo.com')
emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys('not_my_real_email')
emailElem.submit()
passwordElem = browser.find_element_by_id('login-passwd')
passwordElem.send_keys('12345')
passwordElem.submit()

'''
	Se o gmail nao alterou o id dos campos de texto e password, 
	o codigo preenchera esses campos, chamar o metodo submit() em qualquer elemento
	produzira o mesmo resultado que clicar no botao submit do formulario em que o elemento estiver  
'''

*******************************************************************************
********************* enviando caracteres especiais ***************************
*******************************************************************************

O Selenium tem um modulo para teclas que sao impossiveis de digitar em um valor de string
que funciona de modo muito semelhante aos caracteres de escape. Esses valores
sao armazenados em atributos no modulo selenium.webdriver.common.keys
Como esse eh um nome de modulo bem extenso, sera muito mais facil executar from selenium.webdriver.common.keys import Keys
no inicio de seu programa; se fizer isso, voce podera simplesmente escrever Keys em qualquer lugar que devesse normalmente escrever selenium.webdriver.commom.Keys

-------------------------------------------------------------------------
Keys.DOWN,	Keys.UP,	|	As teclas de direcao do teclado.			|
Keys.LEFT,	Keys.RIGHT	|												|
-------------------------------------------------------------------------
Keys.ENTER,	Keys.RETURN	|	As teclas ~ enter e return 					|
-------------------------------------------------------------------------
Keys.HOME,	Keys.END 	|	As teclas ~home, end, pagedown e pageup.	|
Keys.PAGE_DOWN,			|												|
Keys.PAGE_UP			|												|
-------------------------------------------------------------------------
Keys.ESCAPE,			|	As teclas esc, backspace e delete
Keys.BACK_SPACE,		|
Keys.DELETE				|
----------------------------------------------------------------------
Keys.F1		Keys.F2,	|	As teclas de F1 a F12 na parte superior do teclado.
Keys.F12	
-----------------------------------------------------------
Keys.TAB 				|	A tecla tab.
------------------------------------------------------------

Por exemplo, se o cursor nao estiver em um campo de texto no momento, pressionar 
as teclas home e end fara o navegador fazer rolagens para o inicio e o fim 	da pagina.


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http:/nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END) 	#faz rolagens para o fim da pagina
#htmlElem.send_keys(Keys.HOME)	#faz rolagens para o inicio da pagina


'''
	O Selenium tem um modulo para teclas que sao impossiveis de digitar em um valor de string
	que funciona de modo muito semelhante aos caracteres de escape. Esses valores
	sao armazenados em atributos no modulo selenium.webdriver.common.keys
	Como esse eh um nome de modulo bem extenso, sera muito mais facil executar from selenium.webdriver.common.keys import Keys
	no inicio de seu programa; se fizer isso, voce podera simplesmente escrever Keys em qualquer lugar que devesse normalmente escrever selenium.webdriver.commom.Keys
'''



*******************************************************************************
********************* Clicando nos botos do navegador *************************
*******************************************************************************
browser.back()		#clica no botao back (retornar)
browser.forward()	#clica no botao forward (avançar)
browser.refresh()	#clica no botao atualizar/recarregar
browser.quit()		#clica no botao Close Window (fechar janela)





-----------------------------------------------------------------------------
-------------------------	PROGRAMAS	-------------------------------------
-----------------------------------------------------------------------------

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
try:
	elem = browser.find_element_by_class_name('dropdown-menu')
	print('Found <%s> element with that class name!' % (elem.tag_name))
except:
	print('Was not able to find an element with that name.')

'''
	Nesse caso, abrimos o firefox e o direcionamos a um URL. Nessa pagina, tentamos encontrar
	elementos com nome de classe igual a 'dropdown-menu' e, caso esse elemento seja encontrado,
	exibimos seu nome de tag usando o atributo tag_name. Se um elemento desse tipo nao for encontrado,
	exibimos uma mensagem diferente.
'''

----------------------------------------------------------------------------
----------------------------------------------------------------------------

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Forum')
print(type(linkElem))

linkElem.click()	#segue o link "Forum"

'''
	Esses comandos abrem o Firefox em http://inventwithpython.com, obtem o objeto
	WebElement para o elemento <a> com o texto ~ Forum ~ e entao simulam um clique
	nesse elemento <a>. Como se voce mesmo tivesse clicado no link;

'''

----------------------------------------------------------------------------
----------------------------------------------------------------------------

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://mail.yahoo.com')
emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys('not_my_real_email')
emailElem.submit()
passwordElem = browser.find_element_by_id('login-passwd')
passwordElem.send_keys('12345')
passwordElem.submit()

'''
	Se o gmail nao alterou o id dos campos de texto e password, 
	o codigo preenchera esses campos, chamar o metodo submit() em qualquer elemento
	produzira o mesmo resultado que clicar no botao submit do formulario em que o elemento estiver  
'''


----------------------------------------------------------------------------
----------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http:/nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END) 	#faz rolagens para o fim da pagina
#htmlElem.send_keys(Keys.HOME)	#faz rolagens para o inicio da pagina


'''
	O Selenium tem um modulo para teclas que sao impossiveis de digitar em um valor de string
	que funciona de modo muito semelhante aos caracteres de escape. Esses valores
	sao armazenados em atributos no modulo selenium.webdriver.common.keys
	Como esse eh um nome de modulo bem extenso, sera muito mais facil executar from selenium.webdriver.common.keys import Keys
	no inicio de seu programa; se fizer isso, voce podera simplesmente escrever Keys em qualquer lugar que devesse normalmente escrever selenium.webdriver.commom.Keys
'''

----------------------------------------------------------------------------
----------------------------------------------------------------------------
