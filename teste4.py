letra = raw_input('Entre com a letra: ')

vogais = ['a','e','i','o','u']

numeros = ['0','1','2','3','4','5','6','7','8','9']

for a in vogais:
	if(a == letra):
		print "Vogal"
		break 
	else:
		print "diferente de vogal"
		break
	
