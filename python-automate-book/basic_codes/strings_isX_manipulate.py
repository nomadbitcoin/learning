print('hello'.isalpha())		#retornara True se a string for constituida somente de letras e nao estiver vazia
print('hello123'.isalpha())		
print('hello123'.isalnum())		#retornara True se a string for constituida somente de letras e numeros e nao estiver vazia
print('hello'.isalnum())
print('123'.isdecimal())		#retornara True se a string for constituida somente de numeros e nao estiver vazia
print('   '.isspace())			#retornara True se a string for constituida somente de espacos, tabulacoes, quebras de linha e nao estiver vazia
print('This Is Title Case'.istitle())
print('This Is not Title Case 123'.istitle())		#retornara True se a string for constituida somente de palavras que comecem com uma letra maiuscula seguida somente de letras minusculas.
print('This Is NOT Title Case Either'.istitle())