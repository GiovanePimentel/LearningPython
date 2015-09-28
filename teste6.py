numero1 = int(raw_input('Entre com o primeiro numero: '))
numero2 = int(raw_input('Entre com o segundo numero: '))
numero3 = int(raw_input('Entre com o terceiro numero: '))

if(numero1 > numero2):
	if(numero1 > numero3):
		print numero1
	else:
		print numero3
elif(numero2 > numero1):
	if(numero2 > numero3):
		print numero2
	else:
		print numero3

