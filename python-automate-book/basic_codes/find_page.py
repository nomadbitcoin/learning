# page = contents of a web page

page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">'
'<div class="udacity float-left"><a href="http://facebook.com">'
'<div class="udacity float-left"><a href="http://google.com">')

start_link = page.find("<a href=")
start_quote = page.find('"',start_link)
start_end = page.find('"',start_quote+1)
url = page[start_quote+1:start_end]

print url

def func_busca_link():
    start_link1 = page.find("<a href=",start_link+1)
    start_quote1 = page.find('"',start_link1+1)
    start_end1 = page.find('"',start_quote1+1)
    url1 = page[start_quote1+1:start_end1]
    print url1

print func_busca_link()
