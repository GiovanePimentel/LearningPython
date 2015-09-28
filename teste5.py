nota1 = int(raw_input("entre com a primeira nota "))

nota2 = int(raw_input("entre com a segunda nota "))

media =nota1 + nota2

media = float(media)/2
print media

if media >= 7.0:
	print "aprovado"
elif media < 7.0:
	print "reprovado"
elif media == 10.0:
	print "genio"
